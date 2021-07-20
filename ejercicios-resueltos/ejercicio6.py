'''Crer una función que reciba una palabra y te diga cuantas
vocales se encuentran en esa palabra'''

def buscar_vocales(palabra):
    vocales = list('aeiou')
    v = 0
    for p in palabra:
        if (p in vocales):
            v = v + 1
    return v

    
print(buscar_vocales("MAria"))
