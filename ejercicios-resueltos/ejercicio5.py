'''Crea una función que reciba una lista de números y
solo regrese los números pares'''

def pares(lista):
    lis = []
    for l in lista:
        if((l % 2) == 0 ):
            lis.append(l)
    return lis


lista = [1,2,3,4,5,6,7,8,9,10]
print(pares(lista))

    
