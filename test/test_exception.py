from src.exception import PosOcupadaException, MovimientoInvalidoException

def test_exceptions_exist():
    assert issubclass(PosOcupadaException, Exception)
    assert issubclass(MovimientoInvalidoException, Exception)
 
