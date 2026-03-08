import pytest
from calculadora import sumar,restar,multiplicar,dividir

@pytest.mark.parametrize("a,b,esperado",[
    (2,3,5),
    (-1,1,0),
    (2,3,5),
])

#prueba unitaria
def test_sumar():
    """
    Suma dos numeros enteros.
    Parametros:
    a(int): El primer numero a sumar
    a(int): El primer numero a sumar
    a(int): El primer numero a sumar
    Ejemplo

    """
    assert sumar(2,3) == 5
    assert sumar(-1,1) == 0
    assert sumar(0,0) == 0
    with pytest.raises(TypeError):
        sumar("2","3")

    
def test_restar(a:int,b:int) ->int :
    assert sumar(a,b)==esperado
    assert restar(2,2) == 0
    assert restar(2,2) == 0
    assert restar(2,2) == 0
    with pytest.raises(TypeError):
        restar("2","3")

def test_multiplicar():
    assert restar(2,2) == 0
    assert restar(2,2) == 0
    assert restar(2,2) == 0
    with pytest.raises(TypeError):
        restar("2","3")

#pruebas de integracion comprueba integracion vista se renderize frond con back 