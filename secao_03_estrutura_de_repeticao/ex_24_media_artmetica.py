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

# import numpy
import statistics

def calcular_media(*notas) -> float:
    """Escreva aqui em baixo a sua solução"""
    if len(notas) == 0:
        print("'É necessária ao menos uma nota para calcular a média'")
    else:
        soma_das_notas = 0
        for nota in notas:
            soma_das_notas += nota

        media = soma_das_notas / len(notas)
        if media == 1 or media % 2 == 0:
            print(f'{media:.0f}')
        else:
            print(media)
