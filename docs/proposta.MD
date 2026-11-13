# Proposta Inicial do Jogo

Este documento apresenta a proposta inicial do jogo que será desenvolvido pelo grupo utilizando Python e Pygame.

## 1. Nome provisório do jogo

**Nome:** ORÁCULO

## 2. Integrantes do grupo

- Nome 1: Yandi Orlando Santos Rivero
- Nome 2: Giovanni Oliveira Martins Rosa
- Nome 3: Victor Dante Fonseca Oliveira

## 3. Tema escolhido

**Tema:** Inteligência Artificial no Cotidiano — Confiabilidade das recomendações e uso responsável da IA.

**Como esse tema se relaciona com o jogo?**

O jogador recebe recomendações de uma inteligência artificial para resolver desafios, mas essas informações nem sempre são corretas. Ele precisa observar o ambiente, analisar pistas e decidir quando confiar nessa IA, demonstrando a importância de verificar informações produzidas por sistemas inteligentes.

## 4. Tipo de jogo

**Tipo escolhido:** Dungeon crawler 2D com exploração e resolução de puzzles, utilizando gráficos em pixel art e visão superior.

## 5. Descrição geral do jogo

**Descrição:**

O jogador está preso em uma dungeon controlada por uma inteligência artificial chamada Oráculo. Para escapar, deverá atravessar três salas, cada uma contendo um puzzle diferente.

Em cada sala, a IA recomenda uma solução, que pode estar correta ou incorreta. O jogador poderá seguir essa recomendação imediatamente ou investigar pistas presentes no cenário para verificar sua confiabilidade.

Os desafios envolverão a escolha de portas, combinações de alavancas e sequências de símbolos. As soluções poderão variar entre partidas, evitando que o jogador simplesmente memorize as respostas.

Uma escolha incorreta provoca a morte instantânea do personagem, obrigando o jogador a recomeçar a dungeon.

## 6. Objetivo do jogador

**Objetivo:**

Resolver corretamente os puzzles das três salas e escapar da dungeon no menor tempo possível, utilizando as recomendações da IA de maneira crítica e observando as pistas disponíveis no ambiente.

## 7. Regras principais

- **Regra 1:** O jogador deverá atravessar três salas consecutivas, resolvendo um puzzle em cada uma delas.
- **Regra 2:** Em cada sala, a IA fornecerá uma recomendação que poderá estar correta ou incorreta.
- **Regra 3:** O cenário possuirá pistas confiáveis que permitem identificar a solução correta de cada desafio.
- **Regra 4:** Uma escolha incorreta ou uma combinação errada confirmada causará morte instantânea e reiniciará a partida desde a primeira sala.
- **Regra 5:** O tempo será registrado durante a partida, permitindo comparar os melhores resultados. As configurações dos puzzles poderão variar entre partidas.

## 8. Condição de vitória

**Condição de vitória:**

O jogador vence ao resolver corretamente os três puzzles e alcançar a saída da última sala.

Ao concluir o jogo, será exibido seu tempo total, que poderá ser registrado em um ranking de melhores resultados.

## 9. Condição de derrota ou encerramento

**Condição de derrota ou encerramento:**

O jogador perde ao executar uma solução incorreta para qualquer puzzle.

A morte será instantânea, encerrando a tentativa atual. O jogador poderá iniciar uma nova partida desde a primeira sala, com novas configurações dos desafios.

## 10. Elementos previstos no jogo

- **Personagem ou elemento principal:** Personagem controlado pelo jogador, representado em pixel art e capaz de se movimentar pelas salas.
- **Obstáculos ou desafios:** Três puzzles principais: escolha de portas, combinação de alavancas e sequência de símbolos.
- **Itens ou objetos de interação:** Portas, alavancas, inscrições, símbolos, painéis de interação e elementos visuais que fornecem pistas sobre os desafios.
- **Pontuação, vidas, tempo ou progresso:** Cronômetro de partida, indicação da sala atual e ranking de melhores tempos. O personagem terá apenas uma vida por tentativa.

## 11. Controles previstos

**Controles:**

- **W, A, S, D:** Movimentação do personagem pelas salas.
- **E:** Interagir com objetos, investigar pistas, acionar mecanismos e confirmar escolhas.
- **Q:** Consultar novamente a recomendação da IA.
- **R:** Reiniciar a partida após a derrota.
- **Mouse:** Interagir com botões dos menus, caso sejam implementados.

## 12. Principais dificuldades esperadas

- **Dificuldade 1:** Implementar a movimentação do personagem, as colisões com paredes e objetos e as interações utilizando Pygame.
- **Dificuldade 2:** Desenvolver puzzles com soluções variáveis entre partidas, garantindo que as pistas do cenário sejam coerentes com a resposta correta.
- **Dificuldade 3:** Organizar a comunicação entre salas, controlar o cronômetro e implementar o reinício da partida e o armazenamento dos melhores tempos.

## 13. Escopo mínimo para a entrega final

**Escopo mínimo:**

O grupo pretende entregar um jogo 2D funcional utilizando Python e Pygame, contendo:

- Três salas pequenas e jogáveis, com cenários em pixel art.
- Movimentação do personagem e colisões básicas.
- Um puzzle diferente em cada sala.
- Recomendações da IA que poderão estar corretas ou incorretas.
- Pistas investigáveis que permitam resolver os desafios sem depender da sorte.
- Diferentes configurações predefinidas dos puzzles, selecionadas entre partidas.
- Morte instantânea ao executar uma solução incorreta e reinício da dungeon.
- Cronômetro, condição de vitória e registro dos melhores tempos.

A prioridade será desenvolver uma experiência curta, funcional e organizada, evitando mecânicas complexas que possam comprometer a entrega.

## 14. Possíveis melhorias, caso haja tempo

- **Melhoria 1:** Adicionar efeitos sonoros, músicas e animações para melhorar a ambientação.
- **Melhoria 2:** Implementar novas configurações de puzzles e elementos visuais que dificultem a identificação das respostas.
- **Melhoria 3:** Adicionar um menu inicial e uma tela de resultados mais elaborada, com estatísticas das partidas.

## Informações complementares — Organização técnica e originalidade

**Estruturas de dados previstas:**

Serão utilizados principalmente listas e dicionários para armazenar informações sobre as salas, os puzzles, as soluções corretas, as recomendações da IA e as pistas disponíveis.

Cada sala poderá possuir diferentes configurações predefinidas, escolhidas aleatoriamente no início de uma partida. Dessa forma, será possível variar os desafios sem precisar implementar geração procedural de mapas ou inteligência artificial real.

**Organização do código:**

O programa será organizado em funções responsáveis por movimentação, interação, carregamento de salas, verificação das respostas, controle do tempo e gerenciamento dos estados de vitória e derrota. A organização seguirá a estrutura do template oficial da disciplina, podendo incluir módulos auxiliares quando necessário.

**Uso de arquivos:**

Está previsto o armazenamento dos melhores tempos em um arquivo local. As configurações dos puzzles também poderão ser armazenadas em arquivos, caso isso facilite sua organização.

**Testes planejados:**

Serão criados testes simples utilizando `assert` e/ou `pytest` para verificar a escolha das configurações, a validação das soluções dos puzzles, a classificação de acertos e erros e o registro dos resultados. Também serão realizados testes manuais de movimentação, colisões e interações no Pygame.

**Recursos previstos:**

O jogo utilizará Python e Pygame. Os cenários e objetos poderão ser produzidos pelo próprio grupo em pixel art. Caso sejam utilizados recursos externos, suas origens serão identificadas no README do projeto.

**Originalidade:**

O grupo pretende desenvolver uma implementação própria, utilizando o template oficial da disciplina como base. A proposta combina exploração de dungeon, resolução de puzzles e análise crítica de recomendações de IA. Recursos externos eventualmente utilizados serão identificados na documentação do projeto.