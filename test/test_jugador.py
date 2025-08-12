import pytest
from src.jugador import Jugador

def test_jugador_valido():
    j = Jugador("Lau", "X")
    assert j.nombre == "Lau"
    assert j.ficha == "X"

def test_jugador_ficha_invalida():
    with pytest.raises(ValueError):
        Jugador("Valen", "Z")
 
