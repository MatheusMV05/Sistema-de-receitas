def ler_receitas(nome_arquivo): #Lê os nomes das receitas de um arquivo CSV e os retorna como uma lista
    receitas = []
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                receita_info = linha.strip().split(",")  # Remove espaços em branco no início e no fim da linha e separa onde tem virgula
                receitas.append(receita_info)#coleta as informações da receita 
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    return receitas

def salvar_receitas_favoritas(receitas_favoritas, nome_arquivo): #Função para salvar uma lista de nomes de receitas em um arquivo CSV.
    try:
        with open(nome_arquivo, "w") as arquivo: 
            for receita in receitas_favoritas:
                arquivo.write(",".join(receita) + "\n") #Esta parte junta todos os elementos da lista receita em uma única string, separados por vírgulas
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não conseguiu ser aberto!")

def exibir_lista_favoritos(nome_arquivo):
    print("Lista de Favoritos:")
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                receita_info = linha.strip().split(",")
                nome = receita_info[0]
                ingredientes = receita_info[1]
                pais_origem = receita_info[2]
                modo_preparo = receita_info[3]  # Adicionando modo de preparo
                print(f"Nome: {nome}, Ingredientes: {ingredientes}, País de Origem: {pais_origem}, Modo de Preparo: {modo_preparo}")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")

def principal():#Função principal dessa parte
    try:
        receitas = ler_receitas("receitas.csv")  # Lê os nomes das receitas do arquivo "receitas.csv" 
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        return
   
    resposta1 = input("Deseja adicionar as receitas a uma pasta de favoritos? (sim/não): ").lower() #adicionando receitas nessa parte de favoritos
    if resposta1 == "sim":
        receitas_favoritas = []  #lista de receitas favoritas
        for receita in receitas:
            nome = receita[0]  # Adicionando nome
            ingredientes = receita[1]  # Adicionando ingredientes
            pais_origem = receita[2]  # Adicionando pais
            modo_preparo = receita[3]  # Adicionando modo de preparo
            resposta2 = input(f"Deseja adicionar '{nome}' nas receitas favoritas? (sim/não): ").lower()
            if resposta2 == "sim":
                receitas_favoritas.append([nome, ingredientes, pais_origem, modo_preparo])  
        salvar_receitas_favoritas(receitas_favoritas, "receitas_favoritas.csv")
        print("Receitas favoritas salvas com sucesso!")
    else:
        print("As receitas não foram adicionadas ao arquivo!")

if __name__ == "__main__":
    principal()