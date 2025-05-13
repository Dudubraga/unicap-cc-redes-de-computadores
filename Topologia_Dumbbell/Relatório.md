# Relatório de Análise de Desempenho em Topologia Dumbbell

## Introdução
Este relatório apresenta a análise do impacto de delay, perda de pacotes (loss) e algoritmos de controle de congestionamento TCP no desempenho de uma rede utilizando uma topologia do tipo dumbbell. O objetivo é identificar como diferentes combinações de parâmetros afetam a performance da rede e determinar qual algoritmo de congestionamento se comporta melhor em diferentes cenários.

## Metodologia
### Configuração da Topologia
A topologia utilizada consiste em:
- **Clientes**: 2 (Host 1 e Host 2)
- **Roteadores**: 2 (Roteador 1 e Roteador 2)
- **Servidores**: 2 (Host 3 e Host 4)

Cada cliente se comunica com um servidor através dos roteadores. A simulação foi realizada utilizando o **Mininet**.

### Parâmetros Variados
Os seguintes parâmetros foram ajustados durante os testes:
1. **Algoritmos de Congestionamento TCP**: RENO, CUBIC, VEGAS
2. **Delay**: 0ms, 10ms, 100ms
3. **Loss**: 0%, 1%, 5%

### Procedimentos
1. Configuração da topologia dumbbell no Mininet.
2. Variação dos parâmetros.
3. Medição do desempenho da rede em cada cenário:
    - **Transferência de dados**
    - **Largura de banda (Bandwidth)**
4. Registro dos dados.

## Resultados
### Tabelas
#### Algoritmo de Congestionamento TCP: CUBIC

| Delay (ms) | Loss (%) | Transferência (min/avg/max) | Bandwidth (min/avg/max) |
|------------|----------|-----------------------------|-------------------------|
| 0          | 0        | 1.68 / 1.86 / 2.16 GB       | 14.4 / 15.9 / 18.5 GB   |
| 0          | 1        |                             |                         |
| 0          | 5        |                             |                         |
| 10         | 0        |        |       |
| 10         | 1        |        |       |
| 10         | 5        |        |       |
| 100        | 0        |        |       |
| 100        | 1        |        |       |
| 100        | 5        |        |       |

#### Algoritmo de Congestionamento TCP: RENO

| Delay (ms) | Loss (%) | Transferência (min/avg/max) | Bandwidth (min/avg/max) |
|------------|----------|-----------------------------|-------------------------|
| 0          | 0        | 1.68 / 1.86 / 2.16 GB       | 14.4 / 15.9 / 18.5 GB   |
| 0          | 1        |                             |                         |
| 0          | 5        |                             |                         |
| 10         | 0        |        |       |
| 10         | 1        |        |       |
| 10         | 5        |        |       |
| 100        | 0        |        |       |
| 100        | 1        |        |       |
| 100        | 5        |        |       |

#### Algoritmo de Congestionamento TCP: VEGAS

| Delay (ms) | Loss (%) | Transferência (min/avg/max) | Bandwidth (min/avg/max) |
|------------|----------|-----------------------------|-------------------------|
| 0          | 0        | 1.68 / 1.86 / 2.16 GB       | 14.4 / 15.9 / 18.5 GB   |
| 0          | 1        |                             |                         |
| 0          | 5        |                             |                         |
| 10         | 0        |        |       |
| 10         | 1        |        |       |
| 10         | 5        |        |       |
| 100        | 0        |        |       |
| 100        | 1        |        |       |
| 100        | 5        |        |       |

### Gráficos
- 6 grafos
- pra cada algoritmo -> delay x loss (pra transfer e bandwitdth)

## Discussão e Análise
- Qual algoritmo se comporta melhor em cenários com alta latência?
- Qual algoritmo se adapta melhor à perda?
- Como a combinação de delay e loss afeta a performance?

## Conclusão
Com base nos resultados obtidos:
- O algoritmo **[algoritmo]** apresentou melhor desempenho em cenários com alta latência.
- O algoritmo **[algoritmo]** foi mais resiliente à perda de pacotes.
- A combinação de **[delay]** e **[loss]** teve o maior impacto na performance.

Este estudo demonstra a importância de escolher o algoritmo de congestionamento adequado para diferentes condições de rede.
