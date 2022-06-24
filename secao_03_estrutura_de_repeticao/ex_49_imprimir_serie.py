"""
Exercício 49 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre os n termos da Série a seguir:
    
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
    
    Imprima no final a soma da série.
    
    ----------------------------------
    | EXEMPLO                         |
    ----------------------------------
    | ENTRADA:                        |
    | n = 5                           |
    | SAIDA:                          |
    | S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 |
    | soma = 3.393650793650793        |
    ----------------------------------
    

    >>> imprimir_serie(5)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9
    soma = 3.393650793650793
    >>> imprimir_serie(7)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13
    soma = 4.477566877566877
    >>> imprimir_serie(3)
    S = 1/1 + 2/3 + 3/5
    soma = 2.2666666666666666
    >>> imprimir_serie(9)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13 + 8/15 + 9/17
    soma = 5.540311975606093

"""


def imprimir_serie(n):
    """Escreva aqui em baixo a sua solução"""
    # numeros_em_sequencia = 1 (i)
    numeros_em_sequencia = []
    numeros_x = []
    # soma = sum()

    for i in range(1, n+1):
        print(i, end=', ')
        numeros_em_sequencia.append(i)

    for x in range(1, n+1):
        print((x * 2) - 1, end=', ')
        numeros_x.append(x)

    for item in zip(numeros_em_sequencia, numeros_x):
        print(item)

    print(f'S = {numeros_em_sequencia}/{numeros_x}')
    # print(f'soma = {soma}')

    # nao sei o que eu to fazendo
    # saida = 'S = '
    # saida = ''
    # soma = 0
    # for numerador, denominador in zip(range(1, n+1)), range(1, 2*(n+1), 2):
    #     saida += f'{numerador}/{denominador} +'
    #     soma += numerador / denominador
    # saida = saida[:-3]
    # print(f'S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13 + 8/15 + 9/17')
    # print(f'soma = {soma}')


    # zip?