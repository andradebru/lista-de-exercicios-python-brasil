"""
Exercício 44 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


    >>> apurar_votos('1')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Lula              0       0.0%
    2                   Dilma             0       0.0%
    3                   FHC               0       0.0%
    4                   Boulos            1     100.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Lula              1      50.0%
    2                   Dilma             0       0.0%
    3                   FHC               0       0.0%
    4                   Boulos            1      50.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Lula              1      33.3%
    2                   Dilma             1      33.3%
    3                   FHC               0       0.0%
    4                   Boulos            1      33.3%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Lula              1      25.0%
    2                   Dilma             1      25.0%
    3                   FHC               1      25.0%
    4                   Boulos            1      25.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Lula              1      20.0%
    2                   Dilma             1      20.0%
    3                   FHC               1      20.0%
    4                   Boulos            1      20.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      20.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Lula              1      16.7%
    2                   Dilma             1      16.7%
    3                   FHC               1      16.7%
    4                   Boulos            1      16.7%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      16.7%
    6                   Votos Brancos     1      16.7%
    >>> apurar_votos('1', '2', '3', '4', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Lula              1       5.6%
    2                   Dilma             1       5.6%
    3                   FHC               1       5.6%
    4                   Boulos            1       5.6%
    -------------------------------------------------------------------
    5                   Votos Nulos       7      38.9%
    6                   Votos Brancos     7      38.9%


"""
from collections import Counter


def apurar_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
    qtd_votos_1 = 0
    qtd_votos_2 = 0
    qtd_votos_3 = 0
    qtd_votos_4 = 0
    qtd_votos_5 = 0
    qtd_votos_6 = 0

    votos_total = len(votos)

    for voto in votos:
        if voto == '1':
            qtd_votos_1 += 1
        if voto == '2':
            qtd_votos_2 += 1
        if voto == '3':
            qtd_votos_3 += 1
        if voto == '4':
            qtd_votos_4 += 1
        if voto == '5':
            qtd_votos_5 += 1
        if voto == '6':
            qtd_votos_6 += 1

        porcentagem_sobre_total_1 = qtd_votos_1*100 / votos_total
        porcentagem_sobre_total_2 = qtd_votos_2*100 / votos_total
        porcentagem_sobre_total_3 = qtd_votos_3*100 / votos_total
        porcentagem_sobre_total_4 = qtd_votos_4*100 / votos_total
        porcentagem_sobre_total_5 = qtd_votos_5*100 / votos_total
        porcentagem_sobre_total_6 = qtd_votos_6*100 / votos_total

    print(f'Código do Candidato Nome do Candidato Votos Porcentagem sobre total')
    print(f'1                   Lula              {qtd_votos_1}{porcentagem_sobre_total_1:10.1f}%')
    print(f'2                   Dilma             {qtd_votos_2}{porcentagem_sobre_total_2:10.1f}%')
    print(f'3                   FHC               {qtd_votos_3}{porcentagem_sobre_total_3:10.1f}%')
    print(f'4                   Boulos            {qtd_votos_4}{porcentagem_sobre_total_4:10.1f}%')
    print('-------------------------------------------------------------------')
    print(f'5                   Votos Nulos       {qtd_votos_5}{porcentagem_sobre_total_5:10.1f}%')
    print(f'6                   Votos Brancos     {qtd_votos_6}{porcentagem_sobre_total_6:10.1f}%')