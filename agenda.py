import json
import os
import time

def adicionar_contato(contatos, nome_contato, numero_telefone, email_contato):
    contatos[nome_contato] = {"telefone" : numero_telefone, "email" : email_contato}

def remover_contato(contatos, nome_contato):
    try:
        del contatos[nome_contato]
        return True
    except KeyError:
        print("Não é possível deletar um contato inexistente!")
        return False
    
def visualizar_contatos(contatos):
    for contato in contatos:
        print(f'{contato}: {contatos[contato]}')
        print()

def pesquisar_contatos(contatos, nome_contato):
    nome_contato = nome_contato.lower()
    contato_encontrado = False
    for contato in contatos:
        contato2 = contato.lower()
        if nome_contato in contato2:
           print({contato : contatos[contato]})
           contato_encontrado = True
           break
    if contato_encontrado == False:
        print("Contato não encontrado!")

def salvar_lista_contatos(contatos, nome_da_lista_para_ser_salva):
    with open(f'{nome_da_lista_para_ser_salva}', 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)

def carregar_lista_contatos(nome_da_lista_a_ser_carregada):
    with open(f'{nome_da_lista_a_ser_carregada}', 'r') as arquivo:
        return json.load(arquivo)
    
def easter_egg(entrada):
    if entrada.strip().lower() == "o dev do app é um gostoso":
        print("Muito obrigado pelo elogio, isso é uma completa verdade incontestável e absoluta!!")
        print("Pressione Enter para continuar...")
        input()
        return True
    return False

def gerenciar_contatos(contatos, nome_arquivo=None):
    while True:
        os.system("cls" if os.name == 'nt' else "clear")
        print("""- 1 Adicionar contato
- 2 Remover contato
- 3 Visualizar lista de contatos
- 4 Pesquisar contato
- 5 Salvar e sair
- 6 Sair sem salvar""")
        escolha = str(input('-Insira uma opção: '))
        if easter_egg(escolha):
            continue

        if escolha == '1':
            nome_contato = input('Digite o nome do contato:')
            numero_telefone = str(input('Digite o número de telefone de seu contato:'))
            email = str(input("Insira o email de seu contato:"))
            adicionar_contato(contatos, nome_contato, numero_telefone, email)
            print("Contato adicionado com sucesso!")
            print()
            print("Aperte enter para continuar")
            input()

        elif escolha =='2':
            nome_contato = input('Digite o nome do contato:')
            sucesso = remover_contato(contatos, nome_contato)
            if sucesso:
                print("Contato removido com sucesso!")
            print()
            print("Aperte enter para continuar")
            input()

        elif escolha=='3':
            visualizar_contatos(contatos)
            print(f'Pressione enter para continuar')
            input()
        
        elif escolha == '4':
            nome_pesquisa = input("Digite o nome do contato para pesquisar:")
            pesquisar_contatos(contatos, nome_pesquisa)
            input()
            print("Pressione enter para continuar")
            input()

        elif escolha=='5':
            if nome_arquivo is None:
                nome_arquivo = input('Insira o nome do arquivo para salvar:')
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += '.json'
            salvar_lista_contatos(contatos, nome_arquivo)
            print(f"Lista salva como {nome_arquivo} com sucesso!")
            time.sleep(2)
            break

        elif escolha=='6':
            print('Voltando ao menu principal!')
            time.sleep(1)
            break

        else:
            print('Insira uma opção válida!')
            time.sleep(1)

def main():
    while True:
        os.system("cls" if os.name == 'nt' else "clear")
        print("""- 1 Criar uma nova lista de contatos
- 2 Carregar uma lista de contatos existente
- 3 Sair""")
        escolha = input('- Escolha uma opção : ')
        if easter_egg(escolha):
            continue

        if escolha == '1':
            contatos = {}
            gerenciar_contatos(contatos)
            print("Pressione enter para  continuar")
            input()

        elif escolha == '2':
            print("Listas Disponiveis:")
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith(".json")]
            if not arquivos:
                print('Nenhuma lista encontrada!')
                time.sleep(3)
                continue
            for i, arquivo in enumerate(arquivos, 1):
                print(f"{i} {arquivo}")
            escolha = int(input("Escolha uma lista de contatos para carregar (0 se nenhuma): "))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('Insira uma opção válida!')
                time.sleep(1)
                continue
            contatos = carregar_lista_contatos(arquivos[escolha-1])
            gerenciar_contatos(contatos, arquivos[escolha-1])

        elif escolha == '3':
            print('Encerrando programa em:')
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('Programa encerrado!')
            break
        else:
            print('Insira uma opção válida!')
            time.sleep(1)

if __name__ == "__main__":
    main()