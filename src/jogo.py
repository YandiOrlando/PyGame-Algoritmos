
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


def desenhar_pedra(tela):
    """Desenha as paredes e o piso de pedra da dungeon."""

    tela.fill((12, 14, 21))

    pygame.draw.rect(tela, (29, 31, 40), (24, 102, 752, 380))
    pygame.draw.rect(tela, (105, 91, 72), (24, 102, 752, 380), 3)

    # Fileiras de blocos nas paredes superior e laterais.
    for y in range(108, 183, 24):
        deslocamento = 0 if (y // 24) % 2 == 0 else 32
        for x in range(32 - deslocamento, 768, 64):
            pygame.draw.rect(tela, (48, 49, 57), (x, y, 62, 22))
            pygame.draw.line(tela, (62, 62, 68), (x + 3, y + 2), (x + 58, y + 2))
            pygame.draw.line(tela, (27, 29, 36), (x + 2, y + 20), (x + 60, y + 20))

    for lado_x in (31, 745):
        for y in range(190, 458, 42):
            pygame.draw.rect(tela, (43, 45, 53), (lado_x, y, 24, 40))
            pygame.draw.line(tela, (59, 59, 66), (lado_x + 2, y + 2), (lado_x + 21, y + 2))

    # Lajes do piso.
    pygame.draw.rect(tela, (25, 27, 34), (55, 190, 690, 268))
    for linha, y in enumerate(range(192, 458, 34)):
        deslocamento = 0 if linha % 2 == 0 else 26
        for x in range(56 - deslocamento, 745, 52):
            laje = pygame.Rect(x + 2, y + 2, 48, 30)
            tom = 32 + ((linha + x // 52) % 3) * 3
            pygame.draw.rect(tela, (tom, tom + 1, tom + 5), laje, border_radius=3)
            pygame.draw.line(tela, (tom + 7, tom + 7, tom + 10),
                             (laje.x + 4, laje.y + 2), (laje.right - 4, laje.y + 2))

    pygame.draw.rect(tela, (87, 76, 64), (45, 184, 710, 280), 2)


def desenhar_tocha(tela, x, y):
    """Desenha uma tocha acesa na parede."""

    pygame.draw.line(tela, (20, 19, 20), (x, y + 12), (x, y + 34), 10)
    pygame.draw.line(tela, (111, 68, 39), (x, y + 10), (x, y + 33), 6)
    pygame.draw.polygon(
        tela, (255, 150, 48),
        ((x, y - 5), (x - 7, y + 7), (x, y + 12), (x + 7, y + 7))
    )
    pygame.draw.circle(tela, (255, 220, 126), (x, y + 5), 3)
    pygame.draw.circle(tela, (115, 63, 31), (x, y + 35), 7, 2)


def desenhar_porta(tela, porta, segura, fonte):
    """Desenha uma porta de madeira e seus detalhes de perigo."""

    rect = porta["rect"]
    moldura = rect.inflate(20, 30)
    pygame.draw.rect(tela, (17, 18, 24), moldura, border_radius=15)
    pygame.draw.rect(tela, (112, 91, 62), moldura, 3, border_radius=15)
    pygame.draw.rect(tela, (69, 45, 35), rect, border_radius=7)
    pygame.draw.rect(tela, (105, 69, 43), rect.inflate(-8, -4), border_radius=5)

    for x in (rect.x + 29, rect.x + 53, rect.x + 77):
        pygame.draw.line(tela, (67, 45, 34), (x, rect.y + 5), (x, rect.bottom - 5), 2)
    pygame.draw.line(tela, (135, 94, 57), (rect.x + 6, rect.y + 5),
                     (rect.right - 6, rect.y + 5), 2)
    pygame.draw.rect(tela, porta["cor"], (rect.x + 4, rect.y + 4, 5, rect.height - 8))
    pygame.draw.circle(tela, (208, 169, 91), (rect.right - 14, rect.centery), 3)

    nome = fonte.render(porta["nome"].upper(), True, (224, 211, 183))
    placa_nome = pygame.Rect(rect.centerx - 37, 178, 74, 22)
    pygame.draw.rect(tela, (28, 27, 29), placa_nome, border_radius=4)
    tela.blit(nome, (placa_nome.centerx - nome.get_width() // 2, placa_nome.y + 2))

    if not segura:
        pygame.draw.ellipse(tela, (75, 15, 23), (rect.centerx - 25, 211, 38, 12))
        pygame.draw.circle(tela, (130, 25, 35), (rect.centerx - 20, 214), 5)
        pygame.draw.circle(tela, (130, 25, 35), (rect.centerx + 10, 220), 4)
        pygame.draw.circle(tela, (130, 25, 35), (rect.centerx + 27, 212), 3)


def desenhar_jogador(tela, jogador):
    """Desenha o aventureiro dentro da caixa de colisao existente."""

    rect = jogador["rect"]
    pygame.draw.ellipse(tela, (13, 14, 18), (rect.x - 5, rect.bottom - 5, 40, 12))
    pygame.draw.polygon(
        tela, (36, 102, 88),
        ((rect.x + 3, rect.y + 13), (rect.right - 3, rect.y + 13),
         (rect.right, rect.bottom + 2), (rect.x, rect.bottom + 2))
    )
    pygame.draw.circle(tela, (44, 57, 57), (rect.centerx, rect.y + 9), 10)
    pygame.draw.circle(tela, (199, 157, 111), (rect.centerx, rect.y + 10), 6)
    pygame.draw.arc(tela, (27, 37, 43), (rect.centerx - 9, rect.y, 18, 16),
                    0, 3.14, 4)
    pygame.draw.line(tela, (180, 190, 173), (rect.right - 2, rect.y + 18),
                     (rect.right + 4, rect.bottom - 1), 2)


def desenhar_cenario(tela, partida, fonte, titulo):
    """Desenha os elementos e as informacoes da partida."""

    desenhar_pedra(tela)

    pygame.draw.rect(tela, (19, 21, 29), (0, 0, LARGURA_TELA, 96))
    pygame.draw.line(tela, (137, 111, 70), (24, 94), (776, 94), 2)
    pygame.draw.circle(tela, (209, 157, 74), (31, 34), 5)
    desenhar_texto(tela, fonte, "DUNGEON DE DECISOES  |  SALA 01", 46, 22,
                   (192, 179, 152))

    desenhar_tocha(tela, 83, 137)
    desenhar_tocha(tela, 717, 137)

    for porta in portas:
        desenhar_porta(
            tela, porta,
            porta["nome"] == partida["desafio"]["porta_correta"],
            fonte
        )

    pygame.draw.rect(tela, (21, 20, 22), placa.inflate(12, 12), border_radius=5)
    pygame.draw.rect(tela, (110, 77, 45), placa, border_radius=4)
    pygame.draw.rect(tela, (190, 157, 98), placa.inflate(-8, -8), 2, border_radius=3)
    pygame.draw.circle(tela, (213, 182, 113), (placa.x + 9, placa.centery), 2)
    pygame.draw.circle(tela, (213, 182, 113), (placa.right - 9, placa.centery), 2)
    desenhar_texto(tela, fonte, "PISTA [E]", placa.x + 10, placa.y + 11,
                   (245, 220, 164))

    desenhar_jogador(tela, partida["jogador"])

    # Tempo
    if partida["estado"] == "jogando":
        tempo = pygame.time.get_ticks() - partida["inicio"]
    else:
        tempo = partida["tempo_final"]

    desenhar_texto(tela, titulo, "PROTOCOLO ORACULO", 34, 48, (239, 218, 179))
    texto_tempo = fonte.render(f"SALA 1/3  |  {tempo / 1000:.1f}s", True,
                               (223, 215, 198))
    tela.blit(texto_tempo, (LARGURA_TELA - texto_tempo.get_width() - 34, 54))

    pygame.draw.rect(tela, (19, 21, 29), (0, 482, LARGURA_TELA, 118))
    pygame.draw.line(tela, (137, 111, 70), (24, 482), (776, 482), 2)
    recomendacao = partida["desafio"]["porta_ia"]
    desenhar_texto(tela, fonte, f"ORACULO  |  Recomendo a porta {recomendacao}.",
                   34, 493, (255, 210, 112))
    desenhar_texto(tela, fonte, "WASD/Setas: mover  |  E: interagir  |  Q: IA  |  R: reiniciar",
                   34, 521, (173, 177, 188))
    desenhar_texto(tela, fonte, partida["mensagem"], 34, 554, (124, 225, 190))

    if partida["estado"] != "jogando":
        sombra = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
        sombra.fill((5, 6, 12, 175))
        tela.blit(sombra, (0, 0))
        painel = pygame.Rect(LARGURA_TELA // 2 - 175, ALTURA_TELA // 2 - 68, 350, 136)
        pygame.draw.rect(tela, (27, 28, 37), painel, border_radius=10)
        pygame.draw.rect(tela, (153, 125, 79), painel, 2, border_radius=10)

        if partida["estado"] == "derrota":
            mensagem = "VOCE MORREU!"
            cor = (255, 70, 70)
        else:
            mensagem = "SALA CONCLUIDA!"
            cor = (100, 255, 130)

        desenhar_texto(
            tela, titulo, mensagem,
            painel.centerx - 115,
            painel.y + 25,
            cor
        )

        desenhar_texto(
            tela, fonte, "Pressione R para reiniciar.",
            painel.centerx - 115,
            painel.y + 82
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
