# -*- coding: utf-8 -*-
"""Fatorial2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mdg5tdN16UoXFASoz37FWHf-6EOPdz0M
"""

numero = int(input('Digite um numero e descubra a fatorial: '))
fat = 0
result = 1

if numero == 0:
  print(f'A fatorial de {numero} é: 1')

elif numero > 0:
  for numeros in range(numero):
    fat = numeros + 1
    result = result * fat
  print(f'A fatorial de {numero} é: {result}')

else:
  print('Valor digitado não Pode ter fatorial')