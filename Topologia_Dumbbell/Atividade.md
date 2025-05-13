## Análise de Desempenho em Topologia Dumbbell

### Objetivo: 
Analisar o impacto de delay, perda de pacotes (loss) e algoritmo de controle de congestionamento no desempenho da rede utilizando uma topologia do tipo dumbbell.

### Descrição da Topologia:
- 2 clientes (Host A e Host B) → Roteador 1 → Roteador 2 → 2 servidores (Server X e Server Y)
- Cada cliente se comunica com um servidor.
- A simulação pode ser feita no Mininet,

### Parametros para Varias:
1. Delay
    - 0ms
    - 10ms
    - 100ms
1. Loss
    - 0%
    - 1%
    - 5%
1. Algoritmos de Congestionamento TCP
    - RENO
    - CUBIC
    - VEGAS

### Tarefas:
1. Configurar a topologia dumbbell com os dois clientes e dois servidores.
2. Variar os parâmetros conforme a tabela de combinações.
3. Medir o desempenho da rede em cada cenário:
    - Transfer
    - Bandwidth 
4. Registrar os dados em uma planilha/tabela comparativa.
5. Analisar os resultados:
    - Qual algoritmo se comporta melhor em cenários com alta latência?
    - Qual algoritmo se adapta melhor à perda?
    - Como a combinação de delay e loss afeta a performance?
6. Produzir um relatório com os seguintes itens:
    - Introdução à topologia e objetivos
    - Metodologia (como os testes foram feitos)
    - Resultados (tabelas, gráficos comparativos)
    - Discussão e análise crítica
    - Conclusão