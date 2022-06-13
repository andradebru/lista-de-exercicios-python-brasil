"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""
def calcular_nota(prova):
    gabarito = ('Nome','A','B','C','D','E','E','D','C','B','A')
    nome_do_aluno = prova[0]
    total_da_nota = 0
    nome_do_aluno = ''
    for resposta_correta, nota_prova in zip(gabarito, prova):
        if resposta_correta == 'Nome':
            nome_do_aluno = prova[0]
        elif resposta_correta == nota_prova:
            total_da_nota += 1
    return nome_do_aluno, total_da_nota

def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    print('Aluno                 Nota')
    soma_notas = 0
    nota_minima = 99999
    nota_maxima = -1
    media_geral = soma_notas / len(provas)

    for prova in provas:
        nome_do_aluno, total_da_nota = calcular_nota(prova)
        soma_notas += total_da_nota
        if total_da_nota > nota_maxima:
            nota_maxima = total_da_nota
        if total_da_nota < nota_minima:
            nota_minima = total_da_nota

        # print(nome_do_aluno, total_da_nota)
        print(f'{nome_do_aluno}                 {total_da_nota}')
        print('---------------------------')
        print(f'Média geral: {media_geral:.2f}')
        print(f'Maior nota: {nota_minima}')
        print(f'Menor nota: {nota_maxima}')
        # print(f'Total de Alunos: {total_alunos}')
