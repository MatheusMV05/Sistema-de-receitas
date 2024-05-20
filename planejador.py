def planejador_de_refeicoes():
    planejador = []
    receitas = {
    'Frango assado': {'frango': 1, 'limão': 2, 'alho': 3, 'azeite': 1},
    'Macarrão com molho de tomate': {'macarrão': 1, 'tomate': 4, 'cebola': 1, 'alho': 2},
    'Salada Caesar': {'alface': 1, 'croutons': 1, 'parmesão': 0.5, 'molho Caesar': 1}
}
    while True:
        opcao = input("Deseja adicionar uma receita ao plano de refeições (sim ou não)? : ")
        if opcao != 'sim':
            break

        refeicao = input("Digite a refeição (por exemplo, Café da manhã, Almoço, Jantar): ")
        receita = input("Digite o nome da receita: ")
        with open("receitas.txt", "r") as file:
            file.read
            if receita in receitas:
                planejador_de_refeicoes(refeicao, receita)
            else:
                print("Receita não encontrada")
        planejador.append(receita)
        with open("planejador.txt", "w") as file:
            file.write(f"Refeição: {refeicao}; Receita{receita}")

    print("\nPlanejador de Refeições:")
    for refeicao in planejador_de_refeicoes:
        print(f"Refeição: {refeicao}")
        print(f"Receita: {receita}")