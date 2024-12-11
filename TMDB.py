import json
import requests
import os
import argparse

diretorio = "C:/Users/bruvieira/Desktop/Nova_pasta/TMDB_CLI/TMDB_CLI"
nome_arquivo = "filmes.json"
caminho_completo = os.path.join(diretorio, nome_arquivo)



chave = "15cef3dcc7e2b5214f1b868965d0195c"
link = f"https://api.themoviedb.org/3/movie"

def url_requerida(tipo):
    return f"{link}{tipo}?api_key={chave}&language=pt-BR"
def salva_json(tipo):
    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        json.dump(arquivo, ensure_ascii=False, indent=4)
    print(f"O arquivo Json foi salvo ")


def doc_json(tipo):
    url = url_requerida(tipo)

    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            salva_json(tipo)

        elif resposta.status_code == 404:
            print("Desculpe, a pagina não foi encontrada")

        else:
            print(f"Erro ao coletar as informações do site")
    except requests.exceptions.RequestsException as erro:
        print(f"Erro ao conectar com a Api {erro}")


def exibir():
    if os.path.exists(caminho_completo):
        with open (caminho_completo, "r", encoding="utf-8") as arquivo:
            filmes = json.load(arquivo)

            for filme in filmes:
                print(f"Título: {filme['Title']}")
                print(f"Avaliação: {filme['vote_average']}")
                print(f"Lançanto: {filme['relase_date']}")
    else:
        print(f"Arquivo {nome_arquivo} não encontrado.")


def main():
    pass
