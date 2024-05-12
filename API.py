import requests

def get_data_from_api(endpoint, params=None, page=1):
    token = "6b2db1d85ee7091f4c256e1152dd4630"

    headers = {"chave-api-dados": token}

    base_url = "https://api.portaldatransparencia.gov.br/api-de-dados"
    url = f"{base_url}/{endpoint}"

    try:
        params = params or {}
        params['pagina'] = page
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro na solicitação. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Erro na solicitação: {e}")
        return None

# USAR ALGUMA DAS FUNÇÕES ABAIXO NA MAIN

def get_bolsaFBeneficiario_municipio(params, page=1):
    endpoint = "bolsa-familia-sacado-beneficiario-por-municipio"
    return get_data_from_api(endpoint, params, page)

def get_bolsaFamilia_municipio(params, page=1):
    endpoint = "bolsa-familia-por-municipio"
    return get_data_from_api(endpoint, params, page)

def get_bolsaFamilia2_municipio(params, page=1):
    endpoint = "auxilio-brasil-por-municipio"
    return get_data_from_api(endpoint, params, page)

def get_bolsaFamilia3_municipio(params, page=1):
    endpoint = "novo-bolsa-familia-por-municipio"
    return get_data_from_api(endpoint, params, page)

def get_auxilio_brasil_data(params, page=1):
    endpoint = "auxilio-brasil-sacado-beneficiario-por-municipio"
    return get_data_from_api(endpoint, params, page)

def getAuxEmergencial_municipio(params, page=1):
    endpoint = "auxilio-emergencial-por-municipio"
    return get_data_from_api(endpoint, params, page)
