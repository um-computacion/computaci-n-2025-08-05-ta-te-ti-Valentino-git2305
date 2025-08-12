import pytest
from src.tablero import Tablero
from src.exception import PosOcupadaException, MovimientoInvalidoException

def test_tablero_inicia_vacio():
    t = Tablero()
    assert t.grid == [["","",""],["","",""],["","",""]]

def test_poner_ficha_ok():
    t = Tablero()
    t.poner_ficha(1,1,"X")
    assert t.grid[1][1] == "X"

def test_poner_ficha_fuera_de_rango():
    t = Tablero()
    with pytest.raises(MovimientoInvalidoException):
        t.poner_ficha(3,0,"X")

def test_pos_ocupada():
    t = Tablero()
    t.poner_ficha(0,0,"O")
    with pytest.raises(PosOcupadaException):
        t.poner_ficha(0,0,"X")

def test_hay_ganador_fila():
    t = Tablero()
    t.poner_ficha(0,0,"X")
    t.poner_ficha(0,1,"X")
    t.poner_ficha(0,2,"X")
    assert t.hay_ganador() == "X"
 
