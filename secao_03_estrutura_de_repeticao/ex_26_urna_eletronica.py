"""
Exercício 26 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

uma eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
 e ao final mostrar o número de votos de cada candidato.

    >>> calcular_votos()
    Votantes: 0
    Votos no candidato corrupto: 0
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto')
    Votantes: 1
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso')
    Votantes: 2
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 3
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 1
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz', 'corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 6
    Votos no candidato corrupto: 2
    Votos no candidato mentiroso: 2
    Votos no candidato rouba, mas faz: 2

"""


def calcular_votos(*votos):
    """Escreva aqui em baixo a sua solução"""

    votantes = 0
    votos_1 = 0
    votos_2 = 0
    votos_3 = 0

    for voto in votos:
        votantes += 1
        if voto == 'corrupto':
            votos_1 += 1
        if voto == 'mentiroso':
            votos_2 += 1
        if voto == 'rouba, mas faz':
            votos_3 += 1
    if votantes >= 1:
        print(
            f'Votantes: {votantes}\nVotos no candidato corrupto: {votos_1}\nVotos no candidato mentiroso: {votos_2}\nVotos no candidato rouba, mas faz: {votos_3}')
    else:
        print(
            f'Votantes: 0\nVotos no candidato corrupto: 0\nVotos no candidato mentiroso: 0\nVotos no candidato rouba, mas faz: 0')
