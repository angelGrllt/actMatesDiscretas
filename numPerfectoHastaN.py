# -*- coding: utf-8 -*-
"""
PROGRAMA QUE IMPRIME LOS NUMEROS PERFECTOS HASTA "N"

ANGEL GABRIEL GRAILLET ALVAREZ

"""
def es_perfecto(n):
  suma_divisores = 1
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      suma_divisores += i + n // i
  return suma_divisores == n

def imprimir_numeros_perfectos(n):
  print(f"Números perfectos hasta {n}")
  for i in range(2, n + 1):
    if es_perfecto(i):
      print(i)


n = int(input("Ingrese un número: "))

imprimir_numeros_perfectos(n)