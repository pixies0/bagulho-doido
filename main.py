import threading
import time
import sys
import concurrent.futures
from API import *
from data import *

def fetch_data(params, todosDados, lock=None):
    page = 1
    while True:
        try:
            dados = get_bolsaFbeneficiado1_nis(params, page=page)
            if not dados:
                break
            with lock:
                print(f"Obtendo dados da página {page} para os parâmetros: {params}")
                todosDados.extend(dados)
            page += 1
        except Exception as e:
            print(f"Erro na solicitação: {e}")
            print("Conexão recusada pelo servidor. Aguardando 5 segundos antes de tentar novamente...")
            time.sleep(5)
            continue

parametros = generate_params()
# print(parametros)
lock = threading.Lock()

todosDados = []
numThreads = 100

with concurrent.futures.ThreadPoolExecutor(max_workers=numThreads) as executor:
    futures = [executor.submit(fetch_data, params, todosDados,lock) for params in parametros]
    for future in concurrent.futures.as_completed(futures):
        future.result()

for future in futures:
    if not future.done():
        print("Uma ou mais tarefas não foram concluídas")

save_data_to_csv(todosDados, 'bolsa_FamiliaNIS1')
