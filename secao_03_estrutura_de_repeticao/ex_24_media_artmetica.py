"""
Exercício 24 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o mostre a média aritmética de N notas.

    >>> calcular_media()
    'É necessária ao menos uma nota para calcular a média'
    >>> calcular_media(1)
    1
    >>> calcular_media(1, 3)
    2
    >>> calcular_media(1, 3, 3)
    2.3333333333333335

"""

import numpy

def calcular_media(*notas) -> float:
    """Escreva aqui em baixo a sua solução"""
    n = list(*notas)

    if n == []:
        print("'É necessária ao menos uma nota para calcular a média'")
        return

    media = numpy.mean(n)

    print(media)
