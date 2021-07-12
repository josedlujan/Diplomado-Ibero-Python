'''
Crear un programa que imprima una tabla
de multiplicar
'''
def multiplicar(numero):
    print("La tabla del numero",numero)
    for n in range(0,11):
        print(n*numero)

numero = int(input("¿Que tabla de multiplicar necesitas?"))

multiplicar(numero)


