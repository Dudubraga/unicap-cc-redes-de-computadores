#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet()

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='192.168.1.10/24')
    h2 = net.addHost('h2', ip='192.168.2.10/24')
    h3 = net.addHost('h3', ip='192.168.3.10/24')
    h4 = net.addHost('h4', ip='192.168.4.10/24')
    
    info( '*** Add switches\n')
    r1 = net.addHost('r1')
    r2 = net.addHost('r2')
    r3 = net.addHost('r3')
    
    info( '*** Add links\n')
    net.addLink(h1, r1) # LAN1
    net.addLink(h2, r2) # LAN2
    net.addLink(r1, r2) # r1-r2
    net.addLink(h3, r3) # LAN3
    net.addLink(h4, r3) # LAN4
    net.addLink(r2, r3) # r2-r3

    info( '*** Starting network\n')
    net.build()

    info( '*** Starting switches\n')
    r1.setIP('192.168.1.1/24', intf='r1-eth0') # LAN1
    r1.setIP('10.0.0.1/30', intf='r1-eth1') # r1-r2

    r2.setIP('192.168.2.1/24', intf='r2-eth0') # LAN2
    r2.setIP('10.0.0.2/30', intf='r2-eth1') # r2-r1
    r2.setIP('10.0.1.1/30', intf='r2-eth2') # r2-r3

    r3.setIP('192.168.3.1/24', intf='r3-eth0') # LAN3
    r3.setIP('192.168.4.1/24', intf='r3-eth1') # LAN4
    r3.setIP('10.0.1.2/30', intf='r3-eth2') # r3-r2

    info( '*** Post configure switches and hosts\n')
    # o caminho padrao de cada host vai ser o roteador que esta conectado
    h1.cmd('ip route add default via 192.168.1.1')
    h2.cmd('ip route add default via 192.168.2.1')
    h3.cmd('ip route add default via 192.168.3.1')
    h4.cmd('ip route add default via 192.168.4.1')

    info( '*** Habilitando IP forwarding nos roteadores\n')
    for router in [r1, r2, r3]:
        router.cmd('sysctl -w net.ipv4.ip_forward=1')

    # r1 tem caminho para alcancar h2/h3/h4 por r2
    r1.cmd('ip route add 192.168.2.0/24 via 10.0.0.2')
    r1.cmd('ip route add 192.168.3.0/24 via 10.0.0.2')
    r1.cmd('ip route add 192.168.4.0/24 via 10.0.0.2')
    
    # r2 tem caminho pra alcancar h1 por r1 e h3/h4 por r3
    r2.cmd('ip route add 192.168.1.0/24 via 10.0.0.1')
    r2.cmd('ip route add 192.168.3.0/24 via 10.0.1.2')
    r2.cmd('ip route add 192.168.4.0/24 via 10.0.1.2')

    # r3 tem caminho pra alcancar h1/h2 por r2
    r3.cmd('ip route add 192.168.1.0/24 via 10.0.1.1')
    r3.cmd('ip route add 192.168.2.0/24 via 10.0.1.1')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
