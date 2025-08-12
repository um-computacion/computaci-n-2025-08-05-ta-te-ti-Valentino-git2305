class Jugador:
    def __init__(self, nombre: str, ficha: str):
        if ficha not in ("X", "O"):
            raise ValueError("La ficha debe ser 'X' u 'O'.")
        self.nombre = nombre
        self.ficha = ficha

    def __repr__(self) -> str:
        return f"Jugador(nombre={self.nombre!r}, ficha={self.ficha!r})"
 
