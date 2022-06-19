"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""
cardapio = [
    ("Cachorro Quente", "100", 1.2),

]


def get_preco_produto(codigo):
    preco = None
    nome = None
    for (pnome, pcodigo, ppreco) in cardapio:
        if codigo == codigo:
            preco = ppreco
            nome = pnome
            break
    return preco, nome


def imprimir_pedido(lista):
    for codigo, qtd in lista:
        preco, nome = get_preco_produto(codigo)
        print(nome, "|", preco, "|", codigo, "|")


def obter_item_pedido(cod):
    item = None
    for item in pedido:
        nome, codigo, preco, qtd = item
        if cod == codigo:
            return item
            break
    preco, nome = get_preco_produto(cod)
    item = [nome, cod, preco, qtd]
    return item


def fechar_pedido(lista):
    for codigo, qtd in lista:
        # preco, nome = get_preco_produto(codigo)
        item_pedido = obter_item_pedido(codigo)
        qtd_item = item_pedido[3] + qtd
        valor_item = qtd_item * item_pedido[2]

        item_pedido[3] = qtd_item
        item_pedido[4] = valor_item
        pedido.append([nome, codigo, preco, qtd])


def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""
    pedido = []

    codigo = itens[0]
    qtd = itens[1]
    qtd_final = 0
    valor_total = 0

    for

    for qtd in itens:
        qtd_final += 1

    for codigo in itens:
        if codigo == '100':
            valor_total += 1.2
        if codigo == '101':
            valor_total += 1.3
        if codigo == '102':
            valor_total += 1.5
        if codigo == '103':
            valor_total += 1.2
        if codigo == '104':
            valor_total += 1.3
        if codigo == '105':
            valor_total += 1.0

    preco = 0
    if codigo == '100':
        preco = 1.2
    if codigo == '101':
        preco += 1.3
    if codigo == '102':
        preco += 1.5
    if codigo == '103':
        preco += 1.2
    if codigo == '104':
        preco += 1.3
    if codigo == '105':
        preco += 1.0

    print('_____________________________________________________________________________')
    print('|                              RESUMO DA CONTA                              |')
    print('|---------------------------------------------------------------------------|')
    print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')
    print(f'| Cachorro Quente  | {codigo}    | 1.20                |          {qtd} |       {preco:.2f} |')
    print('|---------------------------------------------------------------------------|')
    print(f'| Total Geral:                                    |          {qtd_final} |       {valor_total:.2f} |')
    print('_____________________________________________________________________________')
