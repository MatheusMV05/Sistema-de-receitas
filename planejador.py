def planejador_da_semana(plano_semanal, dia_da_semana, refeicao, receita):
    if dia_da_semana not in plano_semanal:
        plano_semanal[dia_da_semana] = {}
    if refeicao not in plano_semanal[dia_da_semana]:
        plano_semanal[dia_da_semana][refeicao] = []
    plano_semanal[dia_da_semana][refeicao].append(receita)