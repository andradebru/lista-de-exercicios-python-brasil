"""
Exercício 06 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

    >>> data_por_extenso('32', '13', '2000')
    Data inválida.

    >>> data_por_extenso('01', '01', '2000')
    Data de Nascimento: 01/01/2000
    Você nasceu em 01 de Janeiro de 2000.

    >>> data_por_extenso('31', '08', '1950')
    Data de Nascimento: 31/08/1950
    Você nasceu em 31 de Outubro de 1950.

    >>> data_por_extenso('02', '02', '1994')
    Data de Nascimento: 31/08/1950
    Você nasceu em 31 de Outubro de 1950.

    >>> data_por_extenso('05', '10', '1989')
    Data de Nascimento: 31/08/1950
    Você nasceu em 31 de Outubro de 1950.


"""


def data_por_extenso(dia, mes, ano):
    """Escreva aqui embaixo a sua solução"""
