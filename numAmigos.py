# -*- coding: utf-8 -*-
"""
PROGRAMA QUE VERIFICA SI DOS NUMEROS INGRESADOS SON AMIGOS

ANGEL GABRIEL GRAILLET ALVAREZ

"""
def suma_divisores(num):
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
    return suma

def son_amigos(num1, num2):
    suma1 = suma_divisores(num1)
    suma2 = suma_divisores(num2)
    if suma1 == num2 and suma2 == num1:
        return True
    else:
        return False

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if son_amigos(num1, num2):
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")