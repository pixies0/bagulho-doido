import csv
import os
from datetime import datetime


def perCode():

    codigos = [
        # '1702109', # Araguaína
        # '1709500', # Gurupi
        # '1721000', # Palmas
        # '1716109', # Paraíso do Tocantins
        # '1718204', # Porto Nacional
    ]

    params_list = []
    for codigo in codigos:
        for year in range(2019, 2025):
            for month in range(1, 13):
                mesAno = f"{year}{month:02}"  # Formato AAAAMM
                params = {
                    "mesAno": mesAno,
                    "codigoIbge": codigo,
                    "pagina": 1
                }
                params_list.append(params)

    return params_list


def perNis(arquivo):
    params_list = []
    with open(arquivo, 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            nis = linha['NIS']
            for year in range(2019, 2025):
                for month in range(1, 13):
                    anoMesReferencia = f"{year}{month:02}"  # Formato AAAAMM
                    params = {
                        "anoMesReferencia": anoMesReferencia,
                        "nis": nis,
                        "pagina": 1
                    }
                    params_list.append(params)
    return params_list


# Invocar um dos métodos acima
def generate_params():
    return perNis(r'relatorios\teste.csv')


def save_data_to_csv(objetos, endpoint):

    def extract_dataBolsaFAuxEmergencial_municipio(objeto):
        nomeIBGE = objeto['municipio']['nomeIBGE']
        dataReferencia = objeto['dataReferencia']
        data_formatada = datetime.strptime(
            dataReferencia, '%Y-%m-%d').strftime('%m/%Y')
        valor = objeto['valor']
        quantidadeBeneficiados = objeto['quantidadeBeneficiados']
        return [nomeIBGE, data_formatada, valor, quantidadeBeneficiados]

    def extract_dataBeneficiado1(objeto):
        nomeIBGE = objeto['municipio']['nomeIBGE']
        nis = objeto['beneficiarioBolsaFamilia']['nis']
        nome = objeto['beneficiarioBolsaFamilia']['nome']
        dataSaque = objeto['dataSaque']
        valorSaque = objeto['valorSaque']
        return [nomeIBGE, nis, nome, dataSaque, valorSaque]

    def extract_dataBeneficiado2(objeto):
        nomeIBGE = objeto['municipio']['nomeIBGE']
        nis = objeto['beneficiarioAuxilioBrasil']['nis']
        nome = objeto['beneficiarioAuxilioBrasil']['nome']
        dataSaque = objeto['dataSaque']
        valorSaque = objeto['valorSaque']
        return [nomeIBGE, nis, nome, dataSaque, valorSaque]

    def extract_dataBeneficiado3(objeto):
        nomeIBGE = objeto['municipio']['nomeIBGE']
        nis = objeto['beneficiarioNovoBolsaFamilia']['nis']
        nome = objeto['beneficiarioNovoBolsaFamilia']['nome']
        dataMesReferencia = objeto['dataMesReferencia']
        valorSaque = objeto['valorSaque']
        return [nomeIBGE, nis, nome, dataMesReferencia, valorSaque]

    # Usar uma das funções acima [dentro].
    dados = [extract_dataBeneficiado1(objeto) for objeto in objetos]
    # print(dados)

    timestamp = datetime.now().strftime("%H%M")
    nome_arquivo = f'relatorios/{endpoint}_{timestamp}.csv'

    # mode ='w', Abra um arquivo para leitura. (padrão)
    # mode ='r', Abra um arquivo para escrever.  Cria um novo arquivo se ele não existir ou trunca o arquivo se existir'
    # mode = 'x', Abra um arquivo para criação exclusiva.  Se o arquivo já existir, a operação falhará.'
    # mode = 'a', Aberto para anexar no final do arquivo sem truncá-lo.  Cria um novo arquivo se ele não existir.
    # mode = 't', Abra em modo texto.  (padrão)
    # mode = 'b', Abra em modo binário.
    # mode = '+', Abra um arquivo para atualização (leitura e escrita)

    def save_to_csv_bolsaFBeneficiado1(dado, nomeArquivo):
        with open(nomeArquivo, mode='a', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Total de Objetos: ' + str(len(dado))])
            writer.writerow(['Nome IBGE', 'NIS', 'Nome',
                            'Data do Saque', 'Valor do Saque'])
            writer.writerows(dado)
            arquivo.close()

    def save_to_csv_bolsaFBeneficiado2(dado, nomeArquivo):
        with open(nomeArquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Total de Objetos: ' + str(len(dado))])
            writer.writerow(['Nome IBGE', 'NIS', 'Nome',
                            'Data Referência', 'Valor do Saque'])
            writer.writerows(dado)
            arquivo.close()

    def save_to_csv_bolsaFamilia(dado, nomeArquivo):
        with open(nomeArquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Auxílio Bolsa Família'])
            writer.writerow(['Nome IBGE', 'Data Referência',
                            'Valor em R$', 'Nº de Beneficiários'])
            writer.writerows(dado)
            arquivo.close()

    def save_to_csv_auxEmergencial(dado, nomeArquivo):
        with open(nomeArquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Auxílio Emergencial mensal por município'])
            writer.writerow(['Nome IBGE', 'Data Referência',
                            'Valor em R$', 'Nº de Beneficiários'])
            writer.writerows(dado)
            arquivo.close()

    # Usar alguma função de modo de gravação
    save_to_csv_bolsaFBeneficiado1(dados, nome_arquivo)
