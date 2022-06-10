
"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia e valide as seguintes informações:

  Nome: maior que 3 caracteres;
  Idade: entre 0 e 150;
  Salário: maior que zero;
  Sexo: 'f' ou 'm';
  Estado Civil: 's', 'c', 'v', 'd';

    >>> cadastrar_usuario('Renzo', 39, 2000, 'm', 'c')
    Cadastro realizado com sucesso
    >>> cadastrar_usuario('Gil', 1, 2000.05, 'f', 's')
    Cadastro realizado com sucesso
    >>> cadastrar_usuario('Gi', 150, 2000.05, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Gi
    >>> cadastrar_usuario('Ti', -1, 2000.05, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Ti
    Erro: a idade precisa estar entre 0 e 150, não pode ser -1
    >>> cadastrar_usuario('Mi', 151, 0, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    >>> cadastrar_usuario('Mi', 151, 0, 'z', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    Erro: o sexo precisa ser "m" ou "f", não pode ser "z"
    >>> cadastrar_usuario('Mi', 151, 0, 't', 'p')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    Erro: o sexo precisa ser "m" ou "f", não pode ser "t"
    Erro: o estado civil precisa ser "s", "c", "v" ou "d", não pode ser "p"

"""


def cadastrar_usuario(nome: str, idade: int, salario: float, sexo: str, estado_civil: str):
    """Escreva aqui em baixo a sua solução"""
    # nome = input('Nome: ')
    # idade = int(input('Idade: '))
    # salario = float(input('Salario: '))
    # sexo = input('Sexo: ').lower()
    # estado_civil = input('Estado civil: ').lower()
    if len(nome) >= 3 and 0 < idade < 150 and 0 < salario and sexo in ('m', 'f') and estado_civil in ['s','c','v','d']:
        print('Cadastro realizado com sucesso')
    else:
        while len(nome) < 3:
            print(f'Erro: o nome precisa ter 3 letras ou mais, não pode ser {nome}')
            break
        while idade < 0 or idade > 150:
            print(f'Erro: a idade precisa estar entre 0 e 150, não pode ser {idade}')
            break
        while 0 >= salario:
            print(f'Erro: o salário precisa ser positivo, não pode ser {salario}')
            break
        while sexo not in ['m', 'f']:
            print(f'Erro: o sexo precisa ser "m" ou "f", não pode ser "{sexo}"')
            break#meio datado ne...
        while estado_civil not in ['s', 'c', 'v', 'd']:
            print(f'Erro: o estado civil precisa ser "s", "c", "v" ou "d", não pode ser "{estado_civil}"')
            break
