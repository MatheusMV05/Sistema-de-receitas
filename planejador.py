def planejador_de_refeicoes(receitas):
    planejador = []
    while True:
        opcao = input("Deseja adicionar uma receita ao plano de refeições (sim ou não)? : ")
        if opcao.lower()!= 'sim':
            break
        else:
            refeicao = input("Digite a refeição (por exemplo, Café da manhã, Almoço, Jantar): ")
            receita_nome = input("Digite o nome da receita: ")
            for receita in receitas:
                if receita["nome"] == receita_nome:
                    planejador.append({"refeicao": refeicao, "receita": receita_nome})
                    with open("planejador.txt", "a") as file:
                        file.write(f"Refeição: {refeicao}; Receita: {receita_nome}\n")
                    print("Receita adicionada ao plano de refeições com sucesso!")
                    break
    print("\nPlanejador de Refeições:")
    with open("planejador.txt", "r") as file:
        for line in file:
            print(line.strip())

def exibir_planejador():
    print("\nPlanejador de Refeições:")
    with open("planejador.txt", "r") as file:
        for line in file:
            print(line.strip())
