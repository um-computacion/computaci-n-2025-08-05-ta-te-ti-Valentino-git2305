import pytest
from src.main import Tateti
from src.exception import PosOcupadaException

def test_flujo_gana_x():
    juego = Tateti()
    juego.jugar_turno(0,0)  # X
    juego.jugar_turno(1,0)  # O
    juego.jugar_turno(0,1)  # X
    juego.jugar_turno(1,1)  # O
    juego.jugar_turno(0,2)  # X gana
    assert juego.estado == "GANA_X"

def test_no_cambia_turno_jugada_invalida():
    juego = Tateti()
    juego.jugar_turno(0,0)  # X
    # Turno de O; intenta ocupar la misma celda -> inválido, debe seguir siendo O
    with pytest.raises(PosOcupadaException):
        juego.jugar_turno(0,0)
    assert juego.turno == "O"

def test_empate():
    juego = Tateti()
    # Secuencia que llena el tablero sin 3 en línea (empate)
    secuencia = [
        (0,0), (0,1),
        (0,2), (1,1),
        (1,0), (1,2),
        (2,1), (2,0),
        (2,2),
    ]
    for fila, col in secuencia:
        juego.jugar_turno(fila, col)
    assert juego.estado == "EMPATE"
