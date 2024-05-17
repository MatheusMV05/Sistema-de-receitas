import os

def cadastrar_receita(receitas):
    #Cadastrar uma nova receita
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

def exibir_receitas(receitas):
    #Exibir todas as receitas
    for receita in receitas:
        print(f"Nome: {receita['nome']}")
        print(f"País: {receita['pais']}")
        print(f"Ingredientes: {receita['ingredientes']}")
        print(f"Modo de preparo: {receita['modo_preparo']}")
        print("")

def atualizar_receita(receitas):
    #Atualizar uma receita
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
    #Excluir uma receita
    nome = input("Informe o nome da receita a ser excluída: ")
    for i, receita in enumerate(receitas):
        if receita["nome"] == nome:
            del receitas[i]
            print("Receita excluída com sucesso!")
            return
    print("Receita não encontrada")

def filtrar_por_pais(receitas):
    """Filtrar receitas por país"""
    pais = input("Informe o país: ")
    receitas_filtradas = [receita for receita in receitas if receita["pais"] == pais]
    exibir_receitas(receitas_filtradas)

def carregar_receitas():
    #Carregar receitas do arquivo
    receitas = []
    if os.path.exists("receitas.csv"):
        with open("receitas.csv", "r") as file:
            for line in file:
                campos = line.strip().split(",")
                if len(campos) < 4:
                    print(f"Linha inválida: {line}")
                    continue
                receita = {
                    "nome": campos[0],
                    "pais": campos[1],
                    "ingredientes": ",".join(campos[2:-1]),  
                    "modo_preparo": campos[-1]  
                }
                receitas.append(receita)
    return receitas

def salvar_receitas(receitas):
    #Salvar receitas em um arquivo csv
    with open("receitas.csv", "w", newline="") as file:
        file.write("nome,pais,ingredientes,modo_preparo\n")
        for receita in receitas:
            file.write(f"{receita['nome']},{receita['pais']},{receita['ingredientes']},{receita['modo_preparo']}\n")

def sugerir_receita_aleatoria(receitas):
    print("Coloca tua parte aqui fabi")
    
def planejar_refeicao(receitas):
    print("Coloca tua parte aqui claudia")


def exibir_menu():
    #Exibir menu principal
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
    print("6 - Selecionar receita aleatoria")
    print("7 - Planejar refeições")
    print("8 - Sair")

def main():
    #Função principal do sistema de receitas
    global receitas
    receitas = carregar_receitas()
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
            print("Obrigado por usar o sistema de receitas!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
