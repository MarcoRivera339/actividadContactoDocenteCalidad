

#algoritmos de busqueda for para complejidad lineal
def busqueda_lineal(arr,elemento):
    for i in range(len(arr)):
        if arr[i]==elemento:
            return i
    return -1

#busqueda binaria iterativa, necesitamos que los elementos esten ordenados
def busqueda_binaria_iterativa(arr,elemento,izq=0,der=None):
    if not der:
        der=len(arr)-1
    while izq<=der:
        print(arr[izq:der+1])
        medio=(izq+der)//2 
        if arr[medio]==elemento:
            return medio
        elif arr[medio]<elemento:
            izq=medio+1
        else:
            der=medio-1
    return -1

#busqueda binaria recursiva
def busqueda_binaria_recursiva(arr,elemento,izq=0,der=None):
    if not der:
        der=len(arr)-1
    if izq > der: return -1
    medio=(izq+der)//2 
    if arr[medio]==elemento:
            return medio
    elif arr[medio]<elemento:
        return busqueda_binaria_recursiva(arr, elemento, medio+1, der)
    else:
        return busqueda_binaria_recursiva(arr, elemento, izq, medio-1)



arr=[10,20,30,40,50,70,60,80,100,90]
print(busqueda_lineal(arr,30))
arr.sort()
print(busqueda_binaria_iterativa(arr,40))
print(busqueda_binaria_recursiva(arr,40))
