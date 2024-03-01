from pathlib import Path

from pytest import fixture


@fixture
def data_path():
    base_path = Path(__file__).parent / "data"
    return base_path