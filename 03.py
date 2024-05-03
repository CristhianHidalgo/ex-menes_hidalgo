"""
Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente.
"""

def dividir_cero():
    while True:
        try:
            dato_1 = int(input("Ingrese el primer dato: "))
            dato_2 = int(input("Ingrese el segundo dato: "))
            division = dato_1 / dato_2
            break
        except ZeroDivisionError:
            print("No se puede dividir un número entre 0")
    return print(f"El resultado de la division es: {division}")


def suma_error():
    while True:
        try:
            dato_1 = input("Ingrese el primer dato: ")
            dato_2 = input("Ingrese el segundo dato: ")
            suma = int(dato_1) + int(dato_2)
            break
        except ValueError:
            print("No se puede operar un string con un entero")
    return print(f"La suma es: {suma}")

def lista_error():
    lista = []
    cantidad = int(input("Ingrese la cantidad de datos para añadir a la lista: "))
    contador = 1

    while contador <= cantidad:
        numero = int(input("Ingrese un número: "))
        lista.append(numero)
        contador += 1

    while True:
        try:
            indice = int(input("Ingresa el indice a buscar: "))
            buscado = lista[indice]
            break
        except IndexError:
            print("El índice sobrepasa la cantidad de valores de la lista")
    return print(f"El número a es: {buscado}")


dividir_cero()
suma_error()
lista_error()
