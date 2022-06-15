"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""

"""Escreva aqui em baixo a sua solução"""


def descobrir_mais_alto_e_baixo(cadastro):
    cliente_mais_alto = None
    cliente_mais_baixo = None
    maior_altura = None
    menor_altura = None

    for (nome, altura, peso) in cadastro:
        if maior_altura is None or altura > maior_altura:
            cliente_mais_alto = nome
            maior_altura = altura
        if menor_altura is None or altura < menor_altura:
            cliente_mais_baixo = nome
            menor_altura = altura
    return cliente_mais_alto, maior_altura, cliente_mais_baixo, menor_altura


def descobrir_maior_peso(cadastro):
    cliente_menor_peso = None
    cliente_maior_peso = None
    maior_peso = None
    menor_peso = None

    for (nome, altura, peso) in cadastro:
        if menor_peso is None or peso < menor_peso:
            cliente_menor_peso = nome
            menor_peso = peso
        if maior_peso is None or peso > maior_peso:
            cliente_maior_peso = nome
            maior_peso = peso
    return cliente_menor_peso, menor_peso, cliente_maior_peso, maior_peso


def descobrir_medias_altura_peso(cadastro):
    total_altura = 0
    total_peso = 0
    for (nome, altura, peso) in cadastro:
        total_altura += altura
        total_peso += peso

    total_clientes = len(cadastro)
    media_altura = total_altura / total_clientes
    media_peso = total_peso / total_clientes
    return media_altura, media_peso


def obter_input():
    cadastro = []
    inputs = []
    contador = 0
    while True:
        entrada = input("")
        inputs.append(entrada)
        contador += 1
        if entrada == '0':
            break
        if contador == 3:
            nome, altura, peso = inputs
            cadastro.append([nome, int(altura), int(peso)])
            inputs = []
            contador = 0
    return cadastro


def rodar_senso():
    cadastro = obter_input()
    resultado = descobrir_mais_alto_e_baixo(cadastro)
    cliente_mais_alto, maior_altura, cliente_mais_baixo, menor_altura = resultado
    resultado = descobrir_maior_peso(cadastro)
    cliente_menor_peso, menor_peso, cliente_maior_peso, maior_peso = resultado

    media_altura, media_peso = descobrir_medias_altura_peso(cadastro)

    print(f'Cliente mais alto: {cliente_mais_alto}, com {maior_altura} centímetros')
    print(f'Cliente mais baixo: {cliente_mais_baixo}, com {menor_altura} centímetros')
    print(f'Cliente mais magro: {cliente_menor_peso}, com {menor_peso} kilos')
    print(f'Cliente mais gordo: {cliente_maior_peso}, com {maior_peso} kilos')
    print('--------------------------------------------------')
    print(f'Media de altura dos clientes: {media_altura:.1f} centímetros')
    print(f'Media de peso dos clientes: {media_peso:.1f} kilos')
