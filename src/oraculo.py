
import random

PORTAS = ["branca", "azul", "vermelha"]


def criar_desafio():
    """Sorteia a porta segura e a recomendacao da IA."""

    porta_correta = random.choice(PORTAS)

    # A IA pode recomendar a porta correta ou uma incorreta
    if random.choice([True, False]):
        porta_ia = porta_correta
    else:
        alternativas = []

        for porta in PORTAS:
            if porta != porta_correta:
                alternativas.append(porta)

        porta_ia = random.choice(alternativas)

    return {
        "porta_correta": porta_correta,
        "porta_ia": porta_ia,
        "pista": "A porta segura nao possui marcas de sangue."
    }


def verificar_porta(desafio, porta_escolhida):
    """Verifica se o jogador escolheu a porta segura."""

    return porta_escolhida == desafio["porta_correta"]
