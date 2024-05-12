import os

def menu():
    print("\nAgenda de Receitas")
    print("1. Adicionar receita")
    print("2. Listar receitas")
    print("3. Pesquisar receita por nome")
    print("4. Atualizar receita")
    print("5. Excluir receita")
    print("6. Sair\n")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_receita():
    receitas = []

    nome = input("Nome da receita: ")
    pais = input("Essa receita é de qual pais?: ")
    ingredientes = input("Ingredientes (separados por vírgula): ").split(',')
    modopreparo = input("Modo de preparo: ")
    tempo_preparo = int(input("Tempo de preparo (em minutos): "))
    rendimento = float(input("Rendimento: "))

    receita = {
        'nome': nome,
        'ingredientes': ingredientes,
        'modopreparo': modopreparo,
        'tempo_preparo': tempo_preparo,
        'rendimento': rendimento,
        'pais': pais
    }

    receitas.append(receita)

    # Aqui implementar a lógica para salvar as receitas em um arquivo de texto
    # ou em uma lista para serem utilizadas posteriormente

def listar_receitas():
    # Aqui  implementar a lógica para ler as receitas do cadastro
    # (por exemplo, de uma lista ou de um arquivo de texto)
    # e exibi-las na tela
    pass

def pesquisar_receita_por_nome():
    nome = input("Digite o nome da receita: ")

    # Aqui implementar a lógica para pesquisar uma receita pelo nome no cadastro
    # (por exemplo, em uma lista ou em um arquivo de texto)
    # e exibi-la na tela, ou exibir uma mensagem informando que a receita não foi encontrada
    pass

def atualizar_receita():
    pesquisar_receita_por_nome()

    # Se a receita foi encontrada, implementar a lógica para atualizá-la
    # (por exemplo, em uma lista ou em um arquivo de texto)
    pass

def excluir_receita():
    pesquisar_receita_por_nome()

    # Se a receita foi encontrada, implementar a lógica para excluí-la do cadastro
    # (por exemplo, de uma lista ou de um arquivo de texto)
    pass

def main():
    while True:
        limpar_tela()
        menu()

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            adicionar_receita()
        elif opcao == 2:
            listar_receitas()
        elif opcao == 3:
            pesquisar_receita_por_nome()
        elif opcao == 4:
            atualizar_receita()
        elif opcao == 5:
            excluir_receita()
        elif opcao == 6:
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
