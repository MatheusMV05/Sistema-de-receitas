receitas_citadas =['a','b','c','d','e'] 
receitas_favoritas=[]

def favoritos(receitas):   
    resposta= str(input(f"Deseja adicionar '{receitas}' às receitas favoritas? (sim/não): "))
    if resposta == "sim":
         receitas_favoritas.append(receitas)
         print(f"A receita {receitas} foi adicionada na sua lista de receitas favoritas!")
    else:
         print(f"A receita {receitas} não foi adicionada na sua lista de receitas favoritas!")
    
