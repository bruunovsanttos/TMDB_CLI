import json
import requests
import os
import argparse

diretorio =
nome_arquivo = "filmes.json"
caminho_completo = os.path.join(diretorio, nome_arquivo)

def url_requerida(link):
    chave = "15cef3dcc7e2b5214f1b868965d0195c"
    link = f"https://api.themoviedb.org/3/movie?api_key{chave}&language=pt-BR"
    return

    

def doc_json():

    url = url_requerida(link)

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


def exibir():
    pass

def main():
    pass
