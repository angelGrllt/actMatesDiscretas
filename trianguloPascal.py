# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:14:01 2024

@author: ANGEL GABRIEL GRAILLET ALVAREZ

CODIGO QUE GENERA EL TRIANGULO DE PASCAL HASTA "N" FILAS INGRESADAS POR EL USUARIO
"""
def generar_pascal(n):
    pascal = [[0 for _ in range(i+1)] for i in range(n)]
    for i in range(n):
        pascal[i][0] = 1
        pascal[i][i] = 1
    for i in range(2, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

def imprimir_pascal(pascal):
    for fila in pascal:
        print(" ".join(str(num) for num in fila))

n = int(input("Ingrese el número de filas del triángulo de Pascal: "))
pascal = generar_pascal(n)
imprimir_pascal(pascal)