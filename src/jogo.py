
import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
)

from src.funcoes import limitar_valor, verificar_colisao
from src.oraculo import criar_desafio, verificar_porta


# Configuracao das portas
portas = [
    {
        "nome": "branca",
        "cor": (230, 230, 230),
        "rect": pygame.Rect(LARGURA_TELA // 4 - 50, 120, 100, 50)
    },
    {
        "nome": "azul",
        "cor": (60, 120, 230),
        "rect": pygame.Rect(LARGURA_TELA // 2 - 50, 120, 100, 50)
    },
    {
        "nome": "vermelha",
        "cor": (210, 60, 60),
        "rect": pygame.Rect(3 * LARGURA_TELA // 4 - 50, 120, 100, 50)
    }
]

placa = pygame.Rect(70, ALTURA_TELA // 2, 100, 45)


def iniciar_partida():
    """Cria uma nova partida com um desafio aleatorio."""

    jogador = {
        "rect": pygame.Rect(
            LARGURA_TELA // 2 - 15,
            ALTURA_TELA - 180,
            30, 30
        ),
        "cor": (80, 220, 160)
    }

    return {
        "jogador": jogador,
        "desafio": criar_desafio(),
        "estado": "jogando",
        "inicio": pygame.time.get_ticks(),
        "tempo_final": 0,
        "mensagem": "Encontre a porta segura e escape da sala."
    }


def movimentar_jogador(jogador, teclas):
    """Movimenta o jogador dentro dos limites da sala."""

    velocidade = 5

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jogador["rect"].x -= velocidade
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        jogador["rect"].x += velocidade
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        jogador["rect"].y -= velocidade
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        jogador["rect"].y += velocidade

    jogador["rect"].x = limitar_valor(
        jogador["rect"].x,
        45,
        LARGURA_TELA - 45 - jogador["rect"].width
    )

    jogador["rect"].y = limitar_valor(
        jogador["rect"].y,
        190,
        ALTURA_TELA - 135 - jogador["rect"].height
    )


def interagir(partida):
    """Permite investigar a placa ou escolher uma porta."""

    jogador = partida["jogador"]

    # Investigando a pista do cenario
    if verificar_colisao(jogador["rect"], placa.inflate(70, 70)):
        partida["mensagem"] = (
            "PISTA: A porta segura nao possui marcas de sangue!"
        )
        return

    # Verificando a porta escolhida
    for porta in portas:
        area = porta["rect"].inflate(50, 130)

        if verificar_colisao(jogador["rect"], area):

            if verificar_porta(partida["desafio"], porta["nome"]):
                partida["estado"] = "vitoria"
                partida["mensagem"] = "Voce encontrou a porta segura!"
            else:
                partida["estado"] = "derrota"
                partida["mensagem"] = "A porta era perigosa! Voce morreu."

            partida["tempo_final"] = (
                pygame.time.get_ticks() - partida["inicio"]
            )
            return

    partida["mensagem"] = "Aproxime-se de um objeto e pressione E."


def desenhar_texto(tela, fonte, texto, x, y, cor=(255, 255, 255)):
    """Exibe uma mensagem na tela."""

    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, (x, y))


def desenhar_cenario(tela, partida, fonte, titulo):
    """Desenha os elementos e as informacoes da partida."""

    tela.fill((18, 18, 22))  # Cinza quase preto

    # Piso e paredes
    pygame.draw.rect(
        tela, (45, 45, 55),
        (30, 105, LARGURA_TELA - 60, ALTURA_TELA - 225)
    )

    pygame.draw.rect(
        tela, (110, 110, 120),
        (30, 105, LARGURA_TELA - 60, ALTURA_TELA - 225),
        8
    )

    # Desenhando as portas e seus sinais de perigo
    for porta in portas:
        pygame.draw.rect(tela, porta["cor"], porta["rect"])

        desenhar_texto(
            tela, fonte, porta["nome"].upper(),
            porta["rect"].x, 180
        )

        # Portas perigosas apresentam sangue no chao
        if porta["nome"] != partida["desafio"]["porta_correta"]:
            pygame.draw.circle(
                tela, (150, 15, 30),
                (porta["rect"].centerx - 20, 218), 10
            )

            pygame.draw.circle(
                tela, (150, 15, 30),
                (porta["rect"].centerx + 10, 225), 7
            )

            pygame.draw.circle(
                tela, (150, 15, 30),
                (porta["rect"].centerx + 28, 212), 5
            )

    # Placa investigavel
    pygame.draw.rect(tela, (170, 145, 90), placa)
    desenhar_texto(
        tela, fonte, "PISTA [E]",
        placa.x + 4, placa.y + 10
    )

    # Personagem temporario
    pygame.draw.rect(
        tela,
        partida["jogador"]["cor"],
        partida["jogador"]["rect"]
    )

    # Tempo
    if partida["estado"] == "jogando":
        tempo = pygame.time.get_ticks() - partida["inicio"]
    else:
        tempo = partida["tempo_final"]

    desenhar_texto(
        tela, titulo, "PROTOCOLO ORACULO", 35, 20
    )

    desenhar_texto(
        tela, fonte,
        f"Sala 1/3 | Tempo: {tempo / 1000:.1f}s",
        35, 65
    )

    # Recomendacao da IA permanece visivel
    recomendacao = partida["desafio"]["porta_ia"]

    desenhar_texto(
        tela, fonte,
        f"ORACULO: Recomendo entrar na porta {recomendacao}!",
        35, ALTURA_TELA - 108,
        (255, 210, 95)
    )

    desenhar_texto(
        tela, fonte,
        "WASD/Setas: mover | E: interagir | Q: IA | R: reiniciar",
        35, ALTURA_TELA - 75
    )

    # Mensagem da interacao com o cenario
    desenhar_texto(
        tela, fonte,
        partida["mensagem"],
        35, ALTURA_TELA - 42,
        (100, 240, 200)
    )

    if partida["estado"] != "jogando":
        if partida["estado"] == "derrota":
            mensagem = "VOCE MORREU!"
            cor = (255, 70, 70)
        else:
            mensagem = "SALA CONCLUIDA!"
            cor = (100, 255, 130)

        pygame.draw.rect(
            tela, (20, 20, 30),
            (LARGURA_TELA // 2 - 150, ALTURA_TELA // 2 - 50, 300, 100)
        )

        desenhar_texto(
            tela, titulo, mensagem,
            LARGURA_TELA // 2 - 115,
            ALTURA_TELA // 2 - 30,
            cor
        )

        desenhar_texto(
            tela, fonte, "Pressione R para reiniciar.",
            LARGURA_TELA // 2 - 115,
            ALTURA_TELA // 2 + 15
        )


def executar_jogo():
    """Executa o loop principal do jogo."""

    pygame.init()

    tela = pygame.display.set_mode(
        (LARGURA_TELA, ALTURA_TELA)
    )

    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 25)
    titulo = pygame.font.Font(None, 36)

    partida = iniciar_partida()
    rodando = True

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

                elif evento.key == pygame.K_r:
                    partida = iniciar_partida()

                elif partida["estado"] == "jogando":
                    if evento.key == pygame.K_e:
                        interagir(partida)

                    elif evento.key == pygame.K_q:
                        recomendacao = partida["desafio"]["porta_ia"]

                        partida["mensagem"] = (
                            f"ORACULO insiste na porta {recomendacao}."
                        )

        if partida["estado"] == "jogando":
            teclas = pygame.key.get_pressed()
            movimentar_jogador(partida["jogador"], teclas)

        desenhar_cenario(tela, partida, fonte, titulo)
        pygame.display.flip()

    pygame.quit()
