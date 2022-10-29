'''Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:

incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.

incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. 
Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. 

excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.

excluirNome – essa função exclui uma pessoa da agenda.

consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.'''

def incluirNovoNome(name, tel): 
    if type(tel) != list:
        dicTeste[name] = [tel]
    else:
        dicTeste[name] = tel
    while True:
        addMore = int(input("\nQuer adicionar mais? [1] SIM | [2] NÃO\n"))
        if addMore == 1:
            nome = input("\nNome: ").lower().strip()
            tel = input("Telefone(pode ser mais de um): ").split()
            teLista = [int(x) for x in tel] 
            dicTeste[nome] = teLista
        elif addMore == 2:
            print("\nEtapa encerrada")
            break
        else:
            print("[1] ou [2] apenas")
    return dicTeste

def incluirTelefone(book):
    print(f"\n{book}")
    nome = input("Nome da pessoa: ").lower().strip()
    tel = int(input("Telefone que deseja adicionar: ")) 
    while True:
        if nome not in book:
            verif = int(input("Deseja adicionar esse nome na agenda? [1] SIM | [2] NÃO\n"))
            if verif == 1:
                incluirNovoNome(nome, tel)
                break
            elif verif == 2:
                break
        else:
            book[nome].append(tel)
            break
    return book

def excluirTelefone(book):
    print(f"\n{book}")
    who = input("Telefone de qual pessoa? ").lower().strip()
    if len(book[who]) == 1:
        book.pop(who, 'Não foi encontrado')
    else:
        excTel = int(input("Digite o telefone a ser excluído: "))
        book[who].remove(excTel)
    return book

def excluirNome(book):
    print(f"\n{book}")
    pessoa = input("Qual o nome da pessoa? ").lower().strip()
    book.pop(pessoa, 'Não foi encontrado')
    return book

def consultarTelefone(book):
    name = input("\nTelefone de qual pessoa? ").lower().strip()
    return f"Telefone: {book[name]}"

print("[1] - Incluir nome e telefone"); print("[2] - Incluir telefone")
print("[3] - Excluir telefone"); print("[4] - Excluir nome")
print("[5] - Consultar telefone")

comando = int(input("Escolha uma tecla conforme a tabela acima: "))

dicTeste = {
    "rafael": [982674489, 977774366], "manuela": [986344351], "joao": [999763241], "rodrigo": [953338972], "victor": [955554444], "pedro": [983697688, 966663333]
    }

if comando == 1:
    print(incluirNovoNome("denis", [999999999, 985490387]))
elif comando == 2:
    print(incluirTelefone(dicTeste))
elif comando == 3:
    print(excluirTelefone(dicTeste))
elif comando == 4:
    print(excluirNome(dicTeste))
elif comando == 5:
    print(consultarTelefone(dicTeste))
    