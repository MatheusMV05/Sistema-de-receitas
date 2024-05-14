import csv

data = []
header=["Receitas favoritas:"]
data.append(header)

def receitas_favoritas():
    with open('UNIDADE 2\PROJETO PYTHON\receitas.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        receitas = [row[0] for row in leitor_csv]  # Lendo apenas a primeira coluna aqui (depois ver em que coluna estão as receitas)
    
    resposta = input("Deseja adicionar receitas à sua lista de receitas favoritas? (s/n): ").lower()

    if resposta == "sim":
        while True:
            nova_receita = input("Digite o nome da receita (ou deixe em branco para parar): ")
            if nova_receita:
                with open('receitas_favoritas.csv', 'a', newline='', encoding='utf-8') as arquivo_favoritas:
                    escritor_csv = csv.writer(arquivo_favoritas)
                    escritor_csv.writerow([nova_receita])
            else:
                break
        print("Receitas adicionadas manualmente à lista de favoritos com sucesso.")
    elif resposta == "não":
        print("Nenhuma receita foi adicionada manualmente à lista de favoritos.")
    else:
        print("Opção inválida.")

# Chamando a função principal
receitas_favoritas()