"""
Exercício 41 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1                                0
3                                10
6                                15
9                                20
12                               25

    >>> gerar_dados_de_financiamente(1000)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1000.00      0%              1                       R$   1000.00
    R$ 1100.00      10%             3                       R$    366.67
    R$ 1150.00      15%             6                       R$    191.67
    R$ 1200.00      20%             9                       R$    133.33
    R$ 1250.00      25%             12                      R$    104.17
    >>> gerar_dados_de_financiamente(1500)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1500.00      0%              1                       R$   1500.00
    R$ 1650.00      10%             3                       R$    550.00
    R$ 1725.00      15%             6                       R$    287.50
    R$ 1800.00      20%             9                       R$    200.00
    R$ 1875.00      25%             12                      R$    156.25

"""


def gerar_dados_de_financiamente(valor_inicial: float):
    """Escreva aqui em baixo a sua solução"""
    valor_divida_1 = valor_inicial
    valor_divida_3 = valor_inicial * 1.1
    valor_divida_6 = valor_inicial * 1.15
    valor_divida_9 = valor_inicial * 1.2
    valor_divida_12 = valor_inicial * 1.25

    valor_parcela_1 = valor_inicial
    valor_parcela_3 = valor_divida_3 / 3
    valor_parcela_6 = valor_divida_6 / 6
    valor_parcela_9 = valor_divida_9 / 9
    valor_parcela_12 = valor_divida_12 / 12

    print(f'Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
    print(f'R$ {valor_divida_1:7.2f}      0%              1                       R${valor_parcela_1:10.2f}')
    print(f'R$ {valor_divida_3:7.2f}      10%             3                       R${valor_parcela_3:10.2f}')
    print(f'R$ {valor_divida_6:7.2f}      15%             6                       R${valor_parcela_6:10.2f}')
    print(f'R$ {valor_divida_9:7.2f}      20%             9                       R${valor_parcela_9:10.2f}')
    print(f'R$ {valor_divida_12:7.2f}      25%             12                      R${valor_parcela_12:10.2f}')
