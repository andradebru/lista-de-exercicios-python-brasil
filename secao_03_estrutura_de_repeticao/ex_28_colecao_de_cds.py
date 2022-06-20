"""
Exercício 28 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

Mostre os valores monetórios com duas casas decimais..

    >>> from secao_03_estrutura_de_repeticao import ex_28_colecao_de_cds
    >>> entradas = ['1', '1']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 1
    Valor total da coleção: R$ 1.00
    Custo médio dos cds: R$ 1.00
    >>> entradas = ['40', '40', '2']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 2
    Valor total da coleção: R$ 80.00
    Custo médio dos cds: R$ 40.00
    >>> entradas = ['10', '20', '30', '40', '4']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 4
    Valor total da coleção: R$ 100.00
    Custo médio dos cds: R$ 25.00
    >>> entradas = ['10', '20', '30', '3']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 3
    Valor total da coleção: R$ 60.00
    Custo médio dos cds: R$ 20.00

"""


def calcular_estatisticas_colecao_de_cd():
    """Escreva aqui em baixo a sua solução"""
    entradas = ['10', '20', '30', '3']
    entradas_int = []
    for elemento in entradas: #transforma as strings em inteiro e joga na lista vazia criada pra isso
        entradas_int.append(int(elemento))

    numero_cds = entradas_int[-1]
    print(f'Número de cds: {numero_cds}')
    valor_total = sum(entradas_int) - entradas_int[-1]
    print(f'Valor total da coleção: R$ {valor_total:.2f}')
    custo_medio = valor_total / numero_cds
    print(f'Custo médio dos cds: R$ {custo_medio:.2f}')


    # lista = []
    # entradas = input('digite')
    # while True:
    #     lista.append(entradas)
    #     entradas = input('digite')
    #     break
    #
    # numero_cds = int(lista[-1])
    # valor_total = sum(lista) #menos o ultimo numero q eh a qtdd
    # custo_medio = valor_total / (len(lista) - 1)
    #
    # print(f'Número de cds: {numero_cds}')
    # print(f'Valor total da coleção: R$ {valor_total:.2f}')
    # print(f'Custo médio dos cds: R$ {custo_medio:.2f}')