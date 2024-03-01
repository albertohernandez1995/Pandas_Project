# Fixtures: Se suelen declarar en el conftest. Este archivo nos permite segun la localizacion del archivo, que sea usable
# no solo en el mismo directorio, sino en los subdirectorios. La fixture se incluye en el test como argumento de la funcion.
from pathlib import Path

from pytest import fixture


@fixture
def input_path():
    base_path = Path(__file__).parent
    return base_path


# Aqui introducimos la fixture input_path dentro de este test
def test_1(input_path):
    pass
