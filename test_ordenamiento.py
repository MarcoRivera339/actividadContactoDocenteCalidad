import pytest
from ordenamiento import ordenamiento_burbuja


# Lista normal desordenada
def test_ordenamiento_basico():
    arr = [5, 3, 8, 1, 2]
    esperado = [1, 2, 3, 5, 8]
    assert ordenamiento_burbuja(arr) == esperado


# Lista con números negativos y repetidos
def test_ordenamiento_negativos_repetidos():
    arr = [4, -1, 4, 2, -3]
    esperado = [-3, -1, 2, 4, 4]
    assert ordenamiento_burbuja(arr) == esperado


# Caso para romper la función (datos no comparables)
def test_ordenamiento_error_tipo():
    arr = [3, "a", 1]
    with pytest.raises(TypeError):
        ordenamiento_burbuja(arr)