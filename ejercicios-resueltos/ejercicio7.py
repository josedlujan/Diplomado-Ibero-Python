'''''Crear una lista que reciba una lista de números y
te muestre los números positivos'''
lista = [0,-10,-8,9,7,6,-2,4]


def positivos(lista):
    for l in lista:
        if(l>0):
            print(l)

positivos(lista)
