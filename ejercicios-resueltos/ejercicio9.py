'''Escribe un programa que reciba una lista de números y
te devuelva el valor mas pequeño de la lista'''
lista = [9,-10,8,-4,0,100,7]

def menor(lista):
    m = lista[0]
    for l in lista:
        if(l<= m):
            m = l
    return m

print(menor(lista))
            
    
