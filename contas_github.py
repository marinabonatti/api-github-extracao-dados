import requests 

class ContaGitHub:

    """Um usuário qualquer no GitHub."""

    def __init__(self, owner, access_token):
        self.owner = str(owner)
        self.headers = {
            'Authorization': 'Bearer ' + access_token
        }
        self.base_url = 'https://api.github.com'

    def obtem_infos_conta(self):
        """Extrai informações que aparecem na página inicial da conta."""

        url_usuario = f'{self.base_url}/users/{self.owner}'
        r = requests.get(url_usuario,headers = self.headers)
        return r.json()

    def obtem_qtd_repositorios(self):
        """Extrai a quantidade de repositórios associados ao perfil fornecido como 'owner'."""
        return self.obtem_infos_conta()['public_repos']
    
    def calcula_qtd_paginas_repo(self):
        """Extrai a quantidade de páginas de repositórios, com base no número encontrado de
        repositórios e sabendo que cada página exibe 30 repositórios.
        """
        qtd_repositorios = self.obtem_qtd_repositorios()
        paginas = qtd_repositorios/30
        return paginas.__ceil__()

    def extrai_repositorios(self):
        """Extrai repositórios associados ao 'owner'."""

        repositorios = []
        url_repositorios = f'{self.base_url}/users/{self.owner}/repos'

        for pagina in range(1, self.calcula_qtd_paginas_repo()+1):
                try:
                    r = requests.get(f'{url_repositorios}?page={pagina}', headers = self.headers)
                    repositorios.append(r.json())
                except:
                     repositorios.append(None)
        return repositorios
    
    def extrai_infos_repositorios(self, info_desejada):
        """Extrai uma informação específica sobre os repositórios, a ser passada como
         parâmetro.
        """
        informacoes_desejadas = []
        repositorios = self.extrai_repositorios()

        for page in repositorios:
            for repositorio in page:
                informacoes_desejadas.append(repositorio[info_desejada])
        return informacoes_desejadas
    
class ContaPessoalGitHub(ContaGitHub):
    """O usuário detentor do access token de autorização."""

    def cria_novo_repositorio(self,dicionario):
        """Cria novo repositório através de POST. 
        Idealmente o dicionário de parâmetro deve conter 'name'
        (nome do repositório a ser criado), 'private'
        (repositório privado ou público, True ou False)
        e pode conter uma breve 'description' do projeto.
        """
        r = requests.post(f'{self.base_url}/user/repos',
                          json = dicionario,
                          headers = self.headers)
        print(r)

    def exclui_repositorio(self, nome_repo):
        """Exclui repositório através de DELETE, basta fornecer o nome do repositório.
        """
        r = requests.delete(f'{self.base_url}/repos/{self.owner}/{nome_repo}',
                            headers = self.headers)
        print(r)