import random

# Lista de receitas aleatorias
receitas_aleatorias = ([
    {
        "nome": "Feijoada",
        "ingredientes": "Feijão preto, carne de porco, linguiça, bacon, cebola, alho, sal",
        "pais_origem": "Brasil",
        "modo_preparo": "Cozinhe o feijão com as carnes e temperos até ficar bem macio."
    },
    {
        "nome": "Sushi",
        "ingredientes": "Arroz de sushi, alga nori, peixe fresco (salmão, atum, etc.), legumes (como pepino, abacate), vinagre de arroz, açúcar, sal",
        "pais_origem": "Japão",
        "modo_preparo": "Preparar o arroz de sushi, cortar os ingredientes, montar o sushi enrolando na alga nori."
    },
    {
        "nome": "Spaghetti alla Carbonara",
        "ingredientes": "Spaghetti, ovos, queijo parmesão, pancetta ou bacon, pimenta preta",
        "pais_origem": "Itália",
        "modo_preparo": "Cozinhe o spaghetti. Enquanto isso, frite a pancetta ou bacon. Misture ovos e queijo em uma tigela. Misture tudo junto com o spaghetti cozido.",
    },
    {
    "nome": "Tacos",
        "ingredientes": "Tortillas de milho ou trigo, carne (bovina, suína ou frango), cebola, tomate, alface, queijo, pimenta, coentro",
        "pais_origem": "México",
        "modo_preparo": "Cozinhe a carne e tempere com especiarias. Aqueça as tortillas e monte os tacos com os ingredientes desejados."
    },
    {
        "nome": "Risoto de Cogumelos",
        "ingredientes": "Arroz arbóreo, cogumelos (shitake, shimeji, champignon), cebola, alho, caldo de legumes, queijo parmesão, vinho branco",
        "pais_origem": "Itália",
        "modo_preparo": "Refogue a cebola e o alho, adicione o arroz e refogue mais um pouco. Acrescente o vinho branco e, aos poucos, o caldo de legumes. Adicione os cogumelos e o queijo parmesão no final."
    },
    {
        "nome": "Hamburguer",
        "ingredientes": "Carne moída, pão de hambúrguer, queijo, alface, tomate, cebola, ketchup, mostarda",
        "pais_origem": "Estados Unidos",
        "modo_preparo": "Modele a carne em formato de hambúrguer e grelhe. Monte o sanduíche com os ingredientes desejados."
    }
])


# Função para sugerir uma receita aleatória
def sugerir_receita_aleatoria():
    receita_aleatoria = random.choice(receitas_aleatorias)
    print("Nome: ", receita_aleatoria['nome'])
    print("Ingredientes: ", receita_aleatoria['ingredientes'])
    print("País de Origem: ", receita_aleatoria['pais_origem'])
    print("Modo de Preparo: ", receita_aleatoria['modo_preparo'])

# Solicitar sugestão de receita
entrada = input("Digite 1 para receber uma sugestão de receita aleatória: ")
if entrada == '1':
    sugerir_receita_aleatoria()
else:
    print("Opção inválida.")
