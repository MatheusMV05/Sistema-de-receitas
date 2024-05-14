receitas_citadas = ['a', 'b', 'c', 'd']
receitas_favoritas = []

def receitas_favorita(receita):
    resposta = input(f"Você deseja adicionar {receita} às receitas favoritas? (sim/não): ")
    if resposta == 'sim':
        receitas_favoritas.append(receita)
        print(f"A receita {receita} foi adicionada às suas receitas favoritas!")
    else:
        print(f"A receita {receita} não foi adicionada às suas receitas favoritas!")

# Itera sobre cada receita citada anteriormente
for receita in receitas_citadas:
    receitas_favorita(receita)

# Imprime a lista de receitas favoritas atualizada
print("Lista de Receitas Favoritas:")
for receitas_favorita in receitas_favoritas:
    print(receitas_favorita)