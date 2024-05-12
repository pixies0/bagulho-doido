from API import *
from data import *

parametros = generate_params()

dadoDeTodosMeses = []
for mes in parametros:
    page = 1
    while True:
        dado = get_bolsaFamilia_municipio(mes, page=page)
        if not dado:
            break
        print(f"Obtendo dados.. os parâmetros são: {mes}")
        dadoDeTodosMeses.extend(dado)
        page += 1

save_data_to_csv(dadoDeTodosMeses, 'bolsa_familiaAux_municipio')