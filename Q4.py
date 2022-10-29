'''Uma nova  Companhia Energética de Belém pretende disponibilizar em seu site um simulador de consumo com o qual seus clientes poderão estimar o valor de suas contas de energia com base na potência e tempo de uso de seus equipamentos elétricos. Como você está fazendo disciplina de programação e as férias estão chegando, resolveu se candidatar a uma vaga de emprego temporário na empresa, para criar o programa que faráos cálculos apresentados no site. O consumo estimado de energia de cada equipamento de um cliente é calculado a partir do tempo médio de uso (em horas) e da potênciado equipamento (Watts). 

O valor encontrado deve ser dividido por 1000 para que se tenha o consumo em KWH. Somando-se o consumo estimado de todos os equipamentos tem-se o consumo estimado total. Por fim, o valor final estimado da conta dependerá da bandeira em vigor naquele mês (conforme tabela 2) e do valor do ICMS (porcentagem de imposto sobre o valor total). 

Faça então um programa que, tendo a tabela de potência de equipamentos abaixo (tabela 1), receba do usuário: a bandeira em vigor no mês, o valor do ICMS, a quantidade de equipamentos a ser informada e os equipamentos com o tempo médio de uso diário (em horas) e calcule o valor estimado da conta do usuário.'''

dictEquipWatt = {'arcondicionado':1600, 'computador':350,
            'chuveiro':5000, 'ferro':1000, 'lampada':32,
            'lavaroupas':600, 'refrigerador':350,
            'tv':200}

print("\nEquipamento - Potência(W)")
for equip in dictEquipWatt:           #Tabela dos equipamentos/potência
    print(f'{equip} - {dictEquipWatt[equip]}')

dictBandeiraCusto = {'verde':0.5, 
                    'amarela':0.53, 
                    'vermelho':0.56}

print('\nBandeira - Custo(KWH)')            
for band in dictBandeiraCusto:         #Tabela das bandeiras/custo
    print(f'{band} - R${dictBandeiraCusto[band]:.2f}')

bandeira = input("Cor da bandeira: ").lower()
while True:    #Restrição para o percentual estar entre 0-100
    valorICMS = float(input("ICMS(%) em forma decimal: "))
    #Entrada para trasnformar em real dentro do intervalo percentual 
    if valorICMS >= 0 and valorICMS <= 1 :
        break
while True:   #Restrição para o número de equipamentos disponíveis
    quantEquip = int(input("Quantidade de equipamentos: "))
    if quantEquip > 0 and quantEquip < 9:
        break

def consumoKWH(): #Função que retorna o consumo total dos equipamentos
    totalConsumo = 0
    for i in range(quantEquip):  #Entradas e cálculo do consumo total em KWH
        entradaDict = input("Equipamento - Tempo médio de uso(horas): ").lower().split()
        consumo = dictEquipWatt[entradaDict[0]]*float(entradaDict[1]) / 1000
        totalConsumo += consumo
    return totalConsumo

def contaEnergia(): #cálculo da conta energia: custo bandeira e ICMS inseridos
    if bandeira == 'verde':
        conta = consumoKWH()*dictBandeiraCusto[bandeira]
        contaFinal = conta*(valorICMS + 1)
    elif bandeira == 'amarela':
        conta = consumoKWH()*dictBandeiraCusto[bandeira]
        contaFinal = conta*(valorICMS + 1)
    elif bandeira == 'vermelho':
        conta = consumoKWH()*dictBandeiraCusto[bandeira]
        contaFinal = conta*(valorICMS + 1)
    return contaFinal

print('\nValor da conta de energia R$', contaEnergia())
