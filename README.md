# Protocolo ORÁCULO

Projeto final da disciplina de Introdução a Algoritmos, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Giovanni
- Yandi Orlando Santos Rivero
- Luiz Gibim
- Victor Dante

## Estrutura do projeto

- `main.py`: ponto de entrada do jogo.
- `src/`: código principal, regras, movimentação e lógica dos puzzles.
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos de recordes e ranking.
- `tests/`: testes automatizados com pytest.
- `docs/`: documentação e proposta do jogo.

## Descrição do jogo

Protocolo ORÁCULO é um dungeon crawler 2D focado em puzzles e no uso responsável da inteligência artificial.

O jogador precisa escapar de uma dungeon resolvendo desafios. Uma IA fornece recomendações que podem estar corretas ou incorretas, enquanto o cenário apresenta pistas que permitem verificar essas informações.

Atualmente, o jogo possui uma sala demonstrativa com três portas, sendo apenas uma segura.

## Objetivo do jogador

Resolver os puzzles, identificar as recomendações incorretas da IA e escapar da dungeon.

A versão final está planejada para conter três salas, mas a versão atual possui apenas a primeira.

## Regras do jogo

- O jogador deve encontrar a porta segura para avançar.
- A IA recomenda uma porta, mas pode estar errada.
- O cenário contém pistas que ajudam a identificar a escolha correta.
- Escolher uma porta incorreta causa morte instantânea.
- Após vencer ou morrer, o jogador pode reiniciar a partida.
- O tempo da tentativa é registrado.

## Controles

- `WASD` ou `setas`: movimentar o personagem.
- `E`: interagir com portas e objetos.
- `Q`: consultar a recomendação da IA.
- `R`: reiniciar a partida.
- `ESC`: fechar o jogo.

## Como executar o projeto

### 1. Abrir a pasta do projeto

Abra a pasta principal do repositório no VS Code e acesse o terminal.

### 2. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 3. Executar o jogo

```bash
python main.py
```

## Como executar os testes

No terminal, dentro da pasta principal do projeto, execute:

```bash
python -m pytest -v
```

Os testes verificam funções do template original e as regras do puzzle do ORÁCULO.

## Estado atual do projeto

**Ponto de Controle 02 — Versão parcial executável**

Funcionalidades implementadas:

- Janela e loop principal do Pygame.
- Movimentação do personagem.
- Primeira sala com três portas.
- Recomendações da IA que podem estar corretas ou incorretas.
- Pistas visuais e objeto investigável.
- Vitória, morte instantânea e reinício.
- Cronômetro da tentativa.
- Testes automatizados.

**Funcionalidades planejadas para a versão final:**

- Três salas com puzzles diferentes.
- Cenários e personagens em pixel art.
- Variação das soluções dos desafios.
- Ranking de melhores tempos.
- Melhorias visuais e sonoras, caso haja tempo.

## Observações

A implementação atual é uma versão demonstrativa, que será ampliada nas próximas etapas do trabalho.