# Redes de Computadores

### Objetivo da Atividade
Nesta atividade, você irá criar e configurar uma topologia de rede complexa utilizando o Mininet, com múltiplos roteadores e sub-redes. O objetivo é garantir que todos os hosts em diferentes redes possam se comunicar entre si por meio de roteamento estático.

### Descrição da Topologia
Você deverá implementar a seguinte rede no Mininet:
```
Especificações de IPs e Interfaces

h1	-   	192.168.1.10/24	LAN1
h2	-	    192.168.2.10/24	LAN2
h3	-   	192.168.3.10/24	LAN3
h4	-	    192.168.4.10/24	LAN4
r1	r1-eth0	192.168.1.1/24	LAN1
r1	r1-eth1	10.0.0.1/30	    Link r1-r2
r2	r2-eth0	192.168.2.1/24	LAN2
r2	r2-eth1	10.0.0.2/30	    Link r1-r2
r2	r2-eth2	10.0.1.1/30	    Link r2-r3
r3	r3-eth0	10.0.1.2/30	    Link r2-r3
r3	r3-eth1	192.168.3.1/24	LAN3
r3	r3-eth2	192.168.4.1/24	LAN4
```

### Tarefas
1. Criar o script da topologia personalizada em Python utilizando Mininet.
2. Configurar IPs em todos os hosts e roteadores conforme a tabela acima.
3. Habilitar o roteamento IP nos roteadores com sysctl.
4. Adicionar rotas estáticas em todos os roteadores para permitir a comunicação entre todas as sub-redes.
5. Verificar a conectividade entre todos os hosts  o comando ping.

### Comandos úteis
- ifconfig
- links
- route
- ip

### 💡 Dicas Técnicas
- Use rX.cmd("ip route add ...") para configurar as rotas estáticas no script.
- Use rX.cmd("sysctl -w net.ipv4.ip_forward=1") para habilitar o roteamento em cada roteador.
- Adicione comandos de verificação como ip route show e ping direto no terminal ou script.

##### Prof. Assis Tiago de Oliveira Filho