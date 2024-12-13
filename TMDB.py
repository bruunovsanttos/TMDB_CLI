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
    return f"{link}/{tipo}?api_key={chave}&language=pt-BR" #tinha erro sem a barra entre o link e o tipo

def salva_json(dados):
    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)#tem que salvar os dados coletados se não colocar somente o arquivo. se não não salva corretamente
    print(f"O arquivo Json foi salvo ")


def doc_json(tipo):
    url = url_requerida(tipo)

    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            salva_json(dados)#usando os dados como argumento para salvar os dados de forma correta

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

            for filme in filmes.get('results',[]):
                print(f"Título: {filme['title']}")#title estava com letra maiuscula assim não encontrando titulo
                print(f"Descrição: {filme['overview']}")
                print(f"Avaliação: {filme['vote_average']}")
                print(f"Lançanto: {filme['release_date']}\n")#estava errado a escrita como relase e não release
    else:
        print(f"Arquivo {nome_arquivo} não encontrado.")


def main():
    parser = argparse.ArgumentParser(description="Filmes TMDB")
    parser.add_argument('--tipo', choices=["now_playing", "popular", "top_rated", "upcoming"], required= False, help= "Tipo de filmes a serem exibidos(playing(passando), popular(mais populares), top(melhores avaliações), upcoming(vem ai)") #--tipo foi colocado para atender as especificidades do codigo

    args = parser.parse_args()
    tipo = args.tipo
    doc_json(tipo)
    exibir()


if __name__ == "__main__":
    main()
