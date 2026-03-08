
def sumar(a,b):
    if type (a) != int or type (b) != int:
        raise TypeError("Los argumentos deben ser enteros") 
    return a+b

def restar(a,b):
    if type (a) != int or type (b) != int:
        raise TypeError("Los argumentos deben ser enteros") 
    return a-b

def multiplicar(a,b):
    if type (a) != int or type (b) != int:
        raise TypeError("Los argumentos deben ser enteros") 
    return a*b

def dividir(a,b):
    if type (a) != int or type (b) != int:
        raise TypeError("Los argumentos deben ser enteros") 
    return a/b