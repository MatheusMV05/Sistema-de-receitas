import os
import random

def cadastrar_receita(receitas):
    # Cadastrar uma nova receita
    nome = input("Informe o nome da receita: ")
    if not nome:
        print("Nome da receita não pode ser vazio!")
        return
    pais = input("Informe o país de origem: ")
    ingredientes = input("Informe os ingredientes: ")
    modo_preparo = input("Informe o modo de preparo: ")
    receita = {
        "nome": nome,
        "pais": pais,
        "ingredientes": ingredientes,
        "modo_preparo": modo_preparo
    }
    receitas.append(receita)
    print("Receita cadastrada com sucesso!")
    resposta = input("Deseja adicionar essa receita aos favoritos? (s/n): ")
    if resposta.lower() == "s":
        favoritos.append(receita)
        print("Receita adicionada aos favoritos com sucesso!")
        salvar_favoritos(favoritos)
    salvar_receitas(receitas)

def exibir_receitas(receitas):
    # Exibir todas as receitas
    for receita in receitas:
        print(f"Nome: {receita['nome']}")
        print(f"País: {receita['pais']}")
        print(f"Ingredientes: {receita['ingredientes']}")
        print(f"Modo de preparo: {receita['modo_preparo']}")
        print("")

def atualizar_receita(receitas):
    # Atualizar uma receita
    nome = input("Informe o nome da receita a ser atualizada: ")
    for i, receita in enumerate(receitas):
        if receita["nome"] == nome:
            receitas[i]["nome"] = input("Informe o novo nome: ")
            receitas[i]["pais"] = input("Informe o novo país: ")
            receitas[i]["ingredientes"] = input("Informe os novos ingredientes: ")
            receitas[i]["modo_preparo"] = input("Informe o novo modo de preparo: ")
            print("Receita atualizada com sucesso!")
            return
    print("Receita não encontrada")

def excluir_receita(receitas):
    # Input para pegar o nome da receita a ser excluida
    nome = input("Informe o nome da receita a ser excluída: ")
    for i, receita in enumerate(receitas):
        if receita["nome"] == nome:
            del receitas[i]
            print("Receita removida com sucesso!")
            # Removendo a receita do arquivo txt 
            with open("receitas.txt", "w") as file:
                for receita in receitas:
                    file.write(f"{receita['nome']};{receita['pais']};{receita['ingredientes']};{receita['modo_preparo']}\n")
            return
    print("Receita não encontrada")



def carregar_receitas():
    # Carregar receitas do arquivo
    receitas = []
    if os.path.exists("receitas.txt"):
        with open("receitas.txt", "r") as file:
            for line in file:
                campos = line.strip().split(";")
                if len(campos) < 4:
                    print(f"Linha inválida: {line}")
                    continue
                receita = {
                    "nome": campos[0],
                    "pais": campos[1],
                    "ingredientes": campos[2],
                    "modo_preparo": campos[3]
                }
                receitas.append(receita)
    return receitas

def salvar_receitas(receitas):
    # Salvar receitas em um arquivo txt
    with open("receitas.txt", "w") as file:
        for receita in receitas:
            file.write(f"{receita['nome']};{receita['pais']};{receita['ingredientes']};{receita['modo_preparo']}\n")

def adicionar_favorito(receitas, favoritos):
    nome = input("Informe o nome da receita a ser adicionada aos favoritos: ")
    for receita in receitas:
        if receita["nome"] == nome:
            favoritos.append(receita)
            print("Receita adicionada aos favoritos com sucesso!")
            return
    print("Receita não encontrada")

def carregar_favoritos():
    favoritos = []
    if os.path.exists("favoritos.txt"):
        with open("favoritos.txt", "r") as file:
            for line in file:
                campos = line.strip().split(";")
                if len(campos) < 4:
                    print(f"Linha inválida: {line}")
                    continue
                receita = {
                    "nome": campos[0],
                    "pais": campos[1],
                    "ingredientes": campos[2],
                    "modo_preparo": campos[3]
                }
                favoritos.append(receita)
    return favoritos

def salvar_favoritos(favoritos):
    with open("favoritos.txt", "w") as file:
        for receita in favoritos:
            file.write(f"{receita['nome']};{receita['pais']};{receita['ingredientes']};{receita['modo_preparo']}\n")

def exibir_favorito(favoritos):
    for receita in favoritos:
        print(f"Nome: {receita['nome']}")
        print(f"País: {receita['pais']}")
        print(f"Ingredientes: {receita['ingredientes']}")
        print(f"Modo de preparo: {receita['modo_preparo']}")
        print("")

def remover_favorito(favoritos):
    nome = input("Informe o nome da receita a ser removida dos favoritos: ")
    for i, receita in enumerate(favoritos):
        if receita["nome"] == nome:
            del favoritos[i]
            print("Receita removida dos favoritos com sucesso!")
            # Remover a receita do arquivo favoritos.txt
            with open("favoritos.txt", "w") as file:
                for receita in favoritos:
                    file.write(f"{receita['nome']};{receita['pais']};{receita['ingredientes']};{receita['modo_preparo']}\n")
            return
    print("Receita não encontrada")

def submenu_favoritos(receitas, favoritos):
    while True:
        exibir_submenu_favoritos()
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            adicionar_favorito(receitas, favoritos)
            salvar_favoritos(favoritos)
        elif opcao == "2":
            exibir_favorito(favoritos)
        elif opcao == "3":
            remover_favorito(favoritos)
            salvar_favoritos(favoritos)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

def sugerir_receita_aleatoria(aleatorio):
    with open("aleatorio.txt", "r", encoding="utf-8") as file:
        receitas_aleatorias = []
        for line in file:
            campos = line.strip().split(";")
            if len(campos) < 4:
                print(f"Linha inválida: {line}")
                continue
            receita = {
                "nome": campos[0],
                "pais": campos[1],
                "ingredientes": campos[2],
                "modo_preparo": campos[3]
            }
            receitas_aleatorias.append(receita)
    
    # Selecionar uma receita aleatória da lista
    receita_aleatoria = random.choice(receitas_aleatorias)
    
    # Exibir a receita aleatória
    print("Receita sugerida:")
    print(f"Nome: {receita_aleatoria['nome']}")
    print(f"País: {receita_aleatoria['pais']}")
    print(f"Ingredientes: {receita_aleatoria['ingredientes']}")
    print(f"Modo de preparo: {receita_aleatoria['modo_preparo']}")
    print("")

    

def planejar_refeicao(receitas):
    print("Coloca tua parte aqui claudia")

def exibir_submenu_favoritos():
    print("""
███████╗░█████╗░██╗░░░██╗░█████╗░██████╗░██╗████████╗░█████╗░░██████╗
██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗██║╚══██╔══╝██╔══██╗██╔════╝
█████╗░░███████║╚██╗░██╔╝░██║░░██║██████╔╝██║░░░██║░░░██║░░██║╚█████╗░
██╔══╝░░██╔══██║░╚████╔╝░░██║░░██║██╔══██╗██║░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║░░╚██╔╝░░░╚█████╔╝██║░░██║██║░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░╚════╝░╚═════╝░""")
    print("Selecione uma opção:")
    print("1 - Adicionar receita aos favoritos")
    print("2 - Exibir favoritos")
    print("3 - Remover receita dos favoritos")
    print("4 - Voltar")

def exibir_menu():
    # Exibir menu principal
    print("""
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░""")
    print("Selecione uma opção:")
    print("1 - Cadastrar receita")
    print("2 - Exibir receitas")
    print("3 - Atualizar receita")
    print("4 - Excluir receita")
    print("5 - Filtrar receitas por país")
    print("6 - Selecionar uma receita aleatoria")
    print("7 - Planejar refeições")
    print("8 - Favoritos")
    print("9 - Sair")

def main():
    # Função principal do sistema de receitas
    global receitas, favoritos
    receitas = carregar_receitas()
    favoritos = carregar_favoritos()
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            cadastrar_receita(receitas)
            salvar_receitas(receitas)
        elif opcao == "2":
            exibir_receitas(receitas)
        elif opcao == "3":
            atualizar_receita(receitas)
        elif opcao == "4":
            excluir_receita(receitas)
        elif opcao == "5":
            filtrar_por_pais(receitas)
        elif opcao == "6":
            sugerir_receita_aleatoria(receitas)
        elif opcao == "7":
            planejar_refeicao(receitas)
        elif opcao == "8":
            submenu_favoritos(receitas, favoritos)
        elif opcao == "9":
            print("Obrigado por usar o sistema de receitas!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
