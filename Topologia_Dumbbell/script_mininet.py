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

d = '0'
l = 0

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    r2 = net.addHost('r2', cls=Node, ip='10.0.10.1/24')
    r2.cmd('sysctl -w net.ipv4.ip_forward=1')
    r1 = net.addHost('r1', cls=Node, ip='192.168.1.1/24')
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='192.168.1.10/24')
    h4 = net.addHost('h4', cls=Host, ip='10.0.20.20/24')
    h2 = net.addHost('h2', cls=Host, ip='192.168.2.20/24')
    h3 = net.addHost('h3', cls=Host, ip='10.0.10.10/24')

    info( '*** Add links\n')
    net.addLink(r1, r2, cls=TCLink, delay=d, loss=l)
    net.addLink(r2, h3)
    net.addLink(h2, r1)
    net.addLink(r2, h4)
    net.addLink(h1, r1)

    info( '*** Starting network\n')
    net.build()

    r1.cmd('ifconfig r1-eth2 192.168.1.1/24')
    r1.cmd('ifconfig r1-eth1 192.168.2.1/24')
    r1.cmd('ifconfig r1-eth0 150.161.192.1/24')

    r2.cmd('ifconfig r2-eth0 150.161.192.2/24')
    r2.cmd('ifconfig r2-eth1 10.0.10.1/24')
    r2.cmd('ifconfig r2-eth2 10.0.20.1/24')

    h1.cmd('route add default gw 192.168.1.1')
    h2.cmd('route add default gw 192.168.2.1')
    h3.cmd('route add default gw 10.0.10.1')
    h4.cmd('route add default gw 10.0.20.1')

    r1.cmd('route add default gw 150.161.192.2')
    r2.cmd('route add default gw 150.161.192.1')

    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    d = input("Valor do Delay: ") # '0', '10', '100'
    p = int(input("Valor da Perda: ")) # '0', '1', '5'
    setLogLevel( 'info' )
    myNetwork()