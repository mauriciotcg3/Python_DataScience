# -*- coding: utf-8 -*-
"""podioCorrida.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cGab3zkQKZf6_VIHpmeLS7g8teYQUGVV
"""

import numpy as np
import statistics as st

corredor = []
tempo_matriz = np.zeros([3,2])
melhor_corredor = ""
melhor_tempo = 9999
melhor_volta = 0

i = 0

media_lista = []

for i in range(3):
  nome = input('Digite o nome do corredor: ')
  corredor.append(nome)

  for j in range(2):
    tempo = float(input(f'Digite o tempo da {j+1}º volta: '))
    tempo_matriz[i, j] = tempo


print('\n')

for i in range(3):
  soma = 0

  for j in range(2):
    if tempo_matriz.min() < melhor_tempo:
      melhor_corredor = corredor[i]
      melhor_volta = j
      melhor_tempo = tempo_matriz.min()
      print(f'A melhor volta foi do(a) corredor(a): {melhor_corredor}, com o tempo de {melhor_tempo} na volta {j+1}')

    soma = soma + tempo_matriz[i, j]

  media = soma/2
  media_lista.append((corredor[i],media))



media_lista.sort(key=lambda x: x[1])

print("Pódio:")
for i in range(3):
    print(f"{i+1}º Lugar: {media_lista[i][0]} - Média de tempo: {media_lista[i][1]} segundos")

print('A melhor media foi de todas as voltas foi de: ', media_lista[0])