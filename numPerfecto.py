# -*- coding: utf-8 -*-
"""
PROGRAMA QUE DETERMINA SI UN NUMERO INGRESADO ES PERFECTO

ANGEL GABRIEL GRAILLET ALVAREZ

"""

def es_perfecto(num):
    suma = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num // i) == num:
                suma = suma + i + num // i
            else:
                suma = suma + i
            i += 1
    return suma == 2 * num

num = int(input("Ingrese un número: "))
if es_perfecto(num):
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")
    