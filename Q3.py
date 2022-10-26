'''A secretaria da Faculdade de Computação da UFPA precisa de um dicionário de estudantes,   definida   da   seguinte   forma:   

D= {'Darth   Vader':(7.5,8.0,6.5),
    'Han   Solo':(9.0,8.5,9.5),
    'Chewbacca':(3.5,1.0,6.5)}
    onde cada par consiste do nome do estudante e das notas do mesmo. 
Escreva uma função chamada “aprovados” que receba como entrada o dicionário D e imprima o nome dos alunos aprovados. Um aluno é aprovado quando todas as suas notas são maiores que 7. Por exemplo, aprovados(D) deverá imprimir Han Solo.'''

dictNotas = {} 
totalSoma = 0
while True:
    alunoEntrada = input("Nome: ").capitalize()
    notaEntrada = input(f"Notas do {alunoEntrada}: ").split()
    conv_notaEntrada = [float(x) for x in notaEntrada]
    nota = tuple(conv_notaEntrada)
    dictNotas[alunoEntrada] = nota

    perg = input("Aperte [s] caso queira encerrar o programa ou qualquer tecla para continuar: ").lower()
    if perg == 's':
        break
alunosAprovados = []
def aprovados(D):
    for aluno in D:
        for grade in D[aluno]: 
            if grade >= 7 and aluno not in alunosAprovados:
                alunosAprovados.append(aluno)
            if aluno in alunosAprovados and grade < 7:
                alunosAprovados.remove(aluno)   
    return alunosAprovados

print(aprovados(dictNotas))