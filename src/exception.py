class PosOcupadaException(Exception):
    """Se lanza cuando se intenta ocupar una celda ya ocupada."""
    pass


class MovimientoInvalidoException(Exception):
    """Se lanza cuando fila/col están fuera de rango o la ficha es incorrecta."""
    pass

