'''O UFC (Ultimate Fighting Championship) colocará em vigor a partir de julho novos procedimentos para suas pesagens a fim de evitar a desidratação intensa e poupar os seus atletas na semana dos combates. Os lutadores deverão se apresentar para o check in(primeira pesagem de checagem da semana que normalmente acontecem quatro dias antes das lutas) sem estar mais que 8% acima do peso limite de suas categorias. Ou seja, um lutador que for competir na categoria dos meio-pesados (até 93 kg) deverá bater, no máximo, 100 kg no check in. Caso este peso seja extrapolado, o atleta será monitorado de perto pela organização, e, se houver sinais de desidratação até o dia da pesagem oficial, na véspera do evento, a luta será cancelada. 

Faça um programa que recebe como entradas o peso limite inferior e o  peso limite superior de uma categoria e os dados de n possíveis lutadores daquela categoria. De cada lutador devem ser lidos nome e peso em uma linha. Os dados de um lutador devem ser armazenados em uma estrutura de dicionário.

O programa deverá imprimir como saída a quantidade de lutadores que foram aprovados; 
a porcentagem de lutadores que foram reprovados no dia de pesagem; 
e o nome do lutador mais leve aprovado na categoria. Em caso de empate, imprimir o que primeiro ocorrer. Caso não haja nenhum lutador aprovado, imprimir a palavra "vazio" para o nome. Cada saída deverá ser impressa em uma linha.'''

while True:
    limiteInf = int(input("Limite inferior: "))     #Entradas
    limiteSup = int(input("Limite superior: "))
    if limiteInf < limiteSup:
        break
print(f'\n{limiteInf} ----------- {limiteSup}')

dictFighters = {}   #Dicionário criado para armazenamento 

while True:
    fighter = input("Nome e Peso (press 0 and [enter] to stop): ").split()    #Nome e peso na mesma linha
    if fighter[0] == '0':      #Condição para quebrar o loop
        break
    dictFighters[fighter[0]] = int(fighter[1])  #Guardando um valor inteiro dentro da chave 'nome do lutador'

reprovados = []
aprovados = []
lowKG = contagem = 0   #contagem, variável criada para que o segundo 'If' ocorra pelo menos uma vez
for fgt in dictFighters:    #loop criado para percorrer as chaves do dicionário
    contagem += 1
    if dictFighters[fgt] < limiteInf or dictFighters[fgt] > limiteSup:  #Condição para reprovar
        reprovados.append(fgt)
    else:                           #Condição para aprovar
        aprovados.append(fgt)
        if dictFighters[fgt] < lowKG or contagem == 1: #Primeiro que ocorrer, por isso o '<' e não '<='.
            lowKG = dictFighters[fgt]  #Menor peso do dicionário guardado nessa variável
            lowKG_Fighter = fgt     #Nome do lutador com menor peso

if len(dictFighters) == len(reprovados):    #Condição caso não haja aprovados
    print("\nNenhum lutador foi aprovado")
    print("Vazio")

def percentReprovados():    #Função criada para calcular a porcentagem de reprovados
    percent = (len(reprovados) / len(dictFighters))*100
    return f'{percent:.2f}%'

if len(dictFighters) != len(reprovados):    #Condição criada para imprimir as variáveis
    print("\nQuantidade de aprovados: ", len(aprovados))
    print("Porcentagem de reprovados: ", percentReprovados())
    print("Lutador mais leve: ", lowKG_Fighter.capitalize())
    

    
