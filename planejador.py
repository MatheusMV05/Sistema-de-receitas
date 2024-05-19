def planejador_da_semana(plano_semanal, dia_da_semana, refeicao, receita):
    if dia_da_semana not in plano_semanal:
        plano_semanal[dia_da_semana] = {}
    if refeicao not in plano_semanal[dia_da_semana]:
        plano_semanal[dia_da_semana][refeicao] = []
    plano_semanal[dia_da_semana][refeicao].append(receita)

receitas = {'Frango assado': {'frango': 1, 'limão': 2, 'alho': 3, 'azeite': 1},
    'Macarrão com molho de tomate': {'macarrão': 1, 'tomate': 4, 'cebola': 1, 'alho': 2},
    'Salada Caesar': {'alface': 1, 'croutons': 1, 'parmesão': 0.5, 'molho Caesar': 1},}

def planejador_de_receitas():
    plano_semanal = {}
    while True:
        opcao = input("Deseja adicionar uma receita ao plano semanal (sim ou não)? : ")
        if opcao != 'sim':
            break
        dia_da_semana = input("Digite o dia da semana (por exemplo, Segunda-feira): ")
        refeicao = input("Digite a refeição (por exemplo, Café da manhã, Almoço, Jantar): ")
        receita = input("Digite o nome da receita: ")
        if receita in receitas:
            planejador_da_semana(plano_semanal, dia_da_semana, refeicao, receita)
        else:
            print("Receita não encontrada")

    print("\nPlano Semanal:")
    for dia in plano_semanal:
        print(f"\n{dia}:")
        for refeicao in plano_semanal[dia]:
            print(f"{refeicao}: {', '.join(plano_semanal[dia][refeicao])}")