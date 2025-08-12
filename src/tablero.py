from typing import List, Optional
from .exception import PosOcupadaException, MovimientoInvalidoException

class Tablero:
    def __init__(self):
        self._grid: List[List[str]] = [["" for _ in range(3)] for _ in range(3)]

    @property
    def grid(self) -> List[List[str]]:
        # copia superficial para evitar mutaciones externas
        return [row[:] for row in self._grid]

    def poner_ficha(self, fila: int, col: int, ficha: str) -> None:
        self._validar_indices(fila, col)
        if ficha not in ("X", "O"):
            raise MovimientoInvalidoException("Ficha inválida.")
        if self._grid[fila][col] != "":
            raise PosOcupadaException("La posición ya está ocupada.")
        self._grid[fila][col] = ficha

    def hay_ganador(self) -> Optional[str]:
        l = self._grid
        # filas
        for i in range(3):
            if l[i][0] and l[i][0] == l[i][1] == l[i][2]:
                return l[i][0]
        # columnas
        for j in range(3):
            if l[0][j] and l[0][j] == l[1][j] == l[2][j]:
                return l[0][j]
        # diagonales
        if l[1][1]:
            if l[0][0] == l[1][1] == l[2][2]:
                return l[1][1]
            if l[0][2] == l[1][1] == l[2][0]:
                return l[1][1]
        return None

    def lleno(self) -> bool:
        return all(c != "" for r in self._grid for c in r)

    def reset(self) -> None:
        for i in range(3):
            for j in range(3):
                self._grid[i][j] = ""

    def _validar_indices(self, fila: int, col: int) -> None:
        if not (0 <= fila < 3 and 0 <= col < 3):
            raise MovimientoInvalidoException("Coordenadas fuera de rango (0..2).")

    def __str__(self) -> str:
        def fmt(v: str) -> str: return v if v in ("X", "O") else " "
        rows = [" | ".join(fmt(c) for c in row) for row in self._grid]
        return "\n---------\n".join(rows)
 
