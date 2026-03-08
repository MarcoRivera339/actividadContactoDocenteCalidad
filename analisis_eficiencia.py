import time
from itertools import permutations

arr=[i for i in range(1000000)]

def obtener_elemento(arr,index):
    return arr[index]  #O(1)

def busqueda_lineal(arr,elemento):
    for i in range(len(arr)):
        if arr[i]==elemento:
            return i
    return -1

def fibonacci_recursivo(n):
    if n==0 or n==1:
        return 1
    return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)

def permutaciones(arr):
    return list(permutations(arr))

#Complejidad constante
print(obtener_elemento(arr,0))      #O(1)

#Complejidad lineal
inicio=time.time()
print(busqueda_lineal(arr,999999))  #O(0)
fin=time.time()
print(f"Tiempo de ejecucion lineal:{fin-inicio} segundos")

#Complejidad exponencial
inicio=time.time()
print(fibonacci_recursivo(10))
fin=time.time()
print(f"Tiempo de ejecucion exponencial:{fin-inicio} segundos")

#complejidad factorial 
arr=[1,2,3,4,5,6,7,8,9,10,11]
inicio=time.time()
print(permutaciones(arr)[:10])  #O(n!)
fin=time.time()
print(f"Tiempo de ejecucion factorial:{fin-inicio} segundos")

