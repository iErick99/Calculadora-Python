import os

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):

    try:

        c = a / b

    except ZeroDivisionError:
        print("*****No se puede dividir entre 0*****")
    else:
        return c

def multiplicar(a, b):

    return a * b

operaciones = {1 : sumar, 2 : restar, 3 : dividir, 4 : multiplicar}

def switch(opcion, a, b):
    return operaciones[opcion](a,b)
