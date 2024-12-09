import json
import requests
import os
import argparse

diretorio =
nome_arquivo = "filmes.json"
caminho_completo = os.path.join(diretorio, nome_arquivo)

def url_requerida:
    pass
    #colocar aqui o endpoint apra requisição com o requeriments

def salva_json:
    
    url = url_requerida()

    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            pass



        elif resposta.status_code == 404:
            pass
            #colocar not found de forma amigavel
        else:
            print(f"Erro ao coletar as informações do site")
    except requests.exceptions.RequestsException as erro:
        print(f"Erro ao conectar com a Api {erro}")
