
from src.oraculo import PORTAS, criar_desafio, verificar_porta


def test_criar_desafio():
    """Deve criar um desafio com portas validas."""
    desafio = criar_desafio()

    assert desafio["porta_correta"] in PORTAS
    assert desafio["porta_ia"] in PORTAS
    assert desafio["pista"] != ""


def test_porta_correta():
    """Deve aceitar a escolha da porta segura."""
    desafio = {"porta_correta": "azul"}

    assert verificar_porta(desafio, "azul") is True


def test_porta_errada():
    """Deve rejeitar a escolha de portas perigosas."""
    desafio = {"porta_correta": "azul"}

    assert verificar_porta(desafio, "branca") is False
    assert verificar_porta(desafio, "vermelha") is False


def test_ia_pode_acertar(monkeypatch):
    """Deve permitir que a IA recomende a porta correta."""
    escolhas = iter(["azul", True])
    monkeypatch.setattr(
        "src.oraculo.random.choice",
        lambda opcoes: next(escolhas)
    )

    desafio = criar_desafio()

    assert desafio["porta_ia"] == desafio["porta_correta"]


def test_ia_pode_errar(monkeypatch):
    """Deve permitir que a IA recomende uma porta incorreta."""
    escolhas = iter(["azul", False, "branca"])
    monkeypatch.setattr(
        "src.oraculo.random.choice",
        lambda opcoes: next(escolhas)
    )

    desafio = criar_desafio()

    assert desafio["porta_ia"] != desafio["porta_correta"]
