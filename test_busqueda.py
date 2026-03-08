import pytest
from busqueda import busqueda_binaria_recursiva


# Caso normal: elemento encontrado
def test_busqueda_elemento_existente():
    arr = [1, 3, 5, 7, 9]
    assert busqueda_binaria_recursiva(arr, 5) == 2


# Caso: elemento no existe
def test_busqueda_elemento_no_existente():
    arr = [1, 3, 5, 7, 9]
    assert busqueda_binaria_recursiva(arr, 4) == -1


# Caso para romper la función: tipo incorrecto
def test_busqueda_tipo_invalido():
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(TypeError):
        busqueda_binaria_recursiva(arr, "3")