from contas_github import ContaGitHub, ContaPessoalGitHub
from pandas import DataFrame, concat
from pathlib import os
from dotenv import load_dotenv

# Carregando variáveis de ambiente, neste caso: .env

load_dotenv()

access_token = str(os.getenv('access_token'))

# Instancianando contas GitHub

amazon = ContaGitHub('amzn', access_token)
meta = ContaGitHub('facebook', access_token)
spotify = ContaGitHub('spotify', access_token)


def agrupar_infos_desejadas(contagithub):
    '''Agrupa as informações desejadas para o escopo específico desse projeto.
    Pode ser alterada à vontade pelo usuário, desde que traga informações de
    fato contidas na API do GitHub como parâmetro dos métodos de ContaGitHub
    utilizados'''
    

    linguagens = contagithub.extrai_infos_repositorios('language')
    nomes_repo = contagithub.extrai_infos_repositorios('name')
    username = contagithub.obtem_infos_conta()['name']
    lista_username = [username] * contagithub.obtem_qtd_repositorios()
    infos_desejadas = {
        'Perfil': lista_username,
        'Repositório': nomes_repo,
        'Linguagem': linguagens
    }
    return infos_desejadas

# Criando o dataframe

amazon = DataFrame(agrupar_infos_desejadas(amazon))
meta = DataFrame(agrupar_infos_desejadas(meta))
spotify = DataFrame(agrupar_infos_desejadas(spotify))

lista_agregado = [amazon,meta,spotify]
df_agregado = concat(lista_agregado)

# Transformando em csv e salvando na pasta

df_agregado.to_csv('Linguagens de programação - Amazon, Meta e Sportify.csv')