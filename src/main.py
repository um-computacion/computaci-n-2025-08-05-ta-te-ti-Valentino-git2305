from typing import Literal, Optional
from .tablero import Tablero
from .jugador import Jugador
from .exception import PosOcupadaException, MovimientoInvalidoException

EstadoJuego = Literal["EN_CURSO", "GANA_X", "GANA_O", "EMPATE"]

class Tateti:
    def __init__(self, jugador_x: Optional[Jugador] = None, jugador_o: Optional[Jugador] = None):
        self.tablero = Tablero()
        self.jugador_x = jugador_x or Jugador("Jugador X", "X")
        self.jugador_o = jugador_o or Jugador("Jugador O", "O")
        self.turno = "X"
        self.estado: EstadoJuego = "EN_CURSO"

    def jugar_turno(self, fila: int, col: int) -> None:
        if self.estado != "EN_CURSO":
            return
        try:
            self.tablero.poner_ficha(fila, col, self.turno)
        except (PosOcupadaException, MovimientoInvalidoException):
            # No cambia turno si la jugada es inválida
            raise

        ganador = self.tablero.hay_ganador()
        if ganador == "X":
            self.estado = "GANA_X"
        elif ganador == "O":
            self.estado = "GANA_O"
        elif self.tablero.lleno():
            self.estado = "EMPATE"
        else:
            self.turno = "O" if self.turno == "X" else "X"

    def reiniciar(self) -> None:
        self.tablero.reset()
        self.turno = "X"
        self.estado = "EN_CURSO"

    def jugador_actual(self) -> Jugador:
        return self.jugador_x if self.turno == "X" else self.jugador_o


def _imprimir_tablero(tablero: Tablero) -> None:
    print(tablero)

def _imprimir_estado(juego: Tateti) -> None:
    if juego.estado == "EN_CURSO":
        print(f"Turno: {juego.turno}")
    elif juego.estado == "GANA_X":
        print("¡Ganó X!")
    elif juego.estado == "GANA_O":
        print("¡Ganó O!")
    else:
        print("Empate.")

if __name__ == "__main__":
    print("Bienvenidos al Ta-Te-Ti")
    juego = Tateti()
    while juego.estado == "EN_CURSO":
        _imprimir_tablero(juego.tablero)
        _imprimir_estado(juego)
        try:
            fila = int(input("Fila (0-2): "))
            col = int(input("Col (0-2): "))
            juego.jugar_turno(fila, col)
        except Exception as e:
            print(f"Error: {e}")
    _imprimir_tablero(juego.tablero)
    _imprimir_estado(juego)
 
