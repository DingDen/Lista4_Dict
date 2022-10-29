'''A 37ª corrida do Círio acontecerá dia 23 de outubro, no Portal da Amazônia em Belém,largada às 6h. Considerando que há apenas 6 corredores e que foi determinada como regra a quantidade de 10 voltas para cada um dos corredores, escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1º o campeão). O campeão é o que tem a menor média de tempos.'''

dictTempo = {}  #Dicionário para armazenar o tempo de cada volta

#Função para calcular a média tendo o nome do corredor como entrada
def mediaTempo(runner):
    totalSoma = 0
    for soma in dictTempo[runner]:
        totalSoma += soma
    media = round(totalSoma / len(dictTempo[runner]), 2) #Aproximação por 2 casas decimais
    return media

dictMedia = {}  #Dicionário para armazenar as médias

quant = int(input("Quantidade de corredores: "))    #Entrada com o nº de corredores

#Entrada de dados e armazenamento dos mesmos no dicionário
for i in range(quant):
    runnerEntrada = input("Nome do atleta: ")
    tempoSeg = input("Digite o tempo de cada volta em segundos: ").split()

    conv_tempoSeg = [float(x) for x in tempoSeg]  #Conversão de string para float

    dictTempo[runnerEntrada] = conv_tempoSeg    #Armazenamento da lista na chave

    calcMedia = mediaTempo(runnerEntrada)   #Cálculo da média dos tempos

    dictMedia[runnerEntrada] = calcMedia    #Armazenando a média na chave


def bestLap():        #Função para calcular a melhor volta e quem fez ela
    
    #Declaração de variáveis
    best_lap = contador = 0
    
    #Percorrendo as chaves do dicionário
    for runner in dictTempo: 
        for lap in dictTempo[runner]:   #Percorrendo os valores de cada chave
            contador += 1
            if lap < best_lap or contador == 1:  #Volta com menor tempo
                best_lap = lap
                
                pivoRunner = runner     #Guardando o nome do corredor

                #Pegando a volta com melhor tempo
                pivoLap = dictTempo[runner].index(best_lap) 
    
    #Uma tupla com o nome e volta do corredor com melhor tempo                
    return pivoRunner, pivoLap + 1

def runnerRanking():       #Função para criar o ranking
    
    #Declaração das listas
    auxKeys = []
    auxMedia = []

    for i in dictMedia:

        #Armazenando chave e media nas listas declaradas
        auxKeys.append(i)
        auxMedia.append(dictMedia[i])
    
    #Ordenando a lista de médias
    auxMedia.sort()
    
    #Declarando a lista dos corredores rankeados
    auxRanking = []

    #Número de iterações
    for rank in range(len(auxKeys)):
        
        #Percorrendo a lista com os nomes
        for runner in auxKeys:

            #Comparando os valores para armazenar de forma rankeada (do menor pro maior)
            if dictMedia[runner] == auxMedia[rank] and runner not in auxRanking:
                auxRanking.append(runner)
    
    return auxRanking   #Retornando a lista rankeada

rankNum = 0     #Numeração para a saída final

#Imprimindo uma tabela com os dados pedidos
print("\nRANKING FINAL")
print('=-'*20)
for tabela in runnerRanking():
    rankNum += 1
    print(f"{rankNum} - {tabela}")
print(f"\nMelhor volta: {bestLap()[1]}\nCorredor que fez a melhor volta: {bestLap()[0]}")
    
