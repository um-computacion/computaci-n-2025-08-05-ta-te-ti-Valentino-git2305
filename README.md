# Ta-Te-Ti (Tic-Tac-Toe) – Computación

Implementación del juego **Ta-Te-Ti** en Python, con clases separadas y tests automatizados.

## 📂 Estructura

.
├─ src/
│ ├─ init.py
│ ├─ exception.py # Excepciones del dominio
│ ├─ jugador.py # Clase Jugador (nombre, ficha)
│ ├─ tablero.py # Lógica del tablero 3x3
│ └─ main.py # Clase Tateti + CLI
└─ test/
├─ init.py
├─ test_exception.py # Tests de excepciones
├─ test_jugador.py # Tests de Jugador
├─ test_tablero.py # Tests de Tablero
└─ test_main.py # Tests de flujo del juego


## 🧩 Clases

- **Tablero**
  - `poner_ficha(fila, col, ficha)`
  - `hay_ganador() -> Optional[str]` → `"X"`, `"O"` o `None`
  - `lleno() -> bool`, `reset()`
- **Jugador**: `nombre`, `ficha` (`"X"`/`"O"`)
- **Excepciones**: `PosOcupadaException`, `MovimientoInvalidoException`
- **Tateti** (en `src/main.py`)
  - Estado: `"EN_CURSO" | "GANA_X" | "GANA_O" | "EMPATE"`
  - `jugar_turno(fila, col)`, `reiniciar()`, `jugador_actual()`

## ▶️ Ejecutar el juego por consola

> Requisito: **Python 3.11+**

**Windows (PowerShell):**
```powershell
$env:PYTHONPATH = "."
python -m src.main

macOS / Linux:
export PYTHONPATH=.
python -m src.main

✅ Correr los tests
python -m pip install -U pip pytest

Ejecutar tests:
Windows (PowerShell)
$env:PYTHONPATH = "."
python -m pytest -q

macOS / Linux
export PYTHONPATH=.
python -m pytest -q

📝 Decisiones de diseño
El turno no cambia si la jugada es inválida (posición ocupada o fuera de rango).

Tablero.__str__ formatea la grilla para mostrarla en la CLI.

Imports internos con estilo paquete: from .exception import ..., from .tablero import ....

🔧 Requisitos
Python 3.11 o superior

pytest para los tests

👤 Autor: Valentino Molinelli 
Carrera: Ingenieria en informatica
Legajo: 64289
