**Título**: Extração de linguagens de programação nos repositórios do GitHub

**Descrição**:

Este projeto consiste em uma ferramenta de extração de quaisquer informações acerca de perfis do
GitHub. Isso é feito através da API do GitHub (_https://api.github.com_) e por meio da instanciação
de objetos pertencentes à classe _'ContaGitHub'_. 

O escopo principal delineado para o projeto foi a criação de uma tabela '.csv' com informações a respeito das linguagens de programação utilizadas nos repositórios de três empresas: Amazon, Meta e Spotify. Além disso, como funcionalidade adicional também foi desenvolvida uma classe _'ContaPessoalGitHub'_ com métodos para fazer alterações no repositório próprio do usuário - basta que ele forneça um _'access_token'_ válido.

**Funcionalidades**:

1. Extração de informações acerca de perfis no GitHub
2. Extração de informações acerca de repositórios do GitHub
3. Geração de tabelas csv com as informações extraídas
4. _(Adicional) Alteração de repositórios do GitHub_

**Exemplos de uso**:

1. Extração de quaisquer dados presentes em repositórios ou perfis do GitHub
2. Análise de tendências (neste caso, linguagens de programação)
3. _(Adicional) Alteração de repositórios do GitHub_

**Tutorial**:

Para fazer uso desse projeto, é necessário obter um _'access_token'_. Para isso, siga os passos abaixo:

1. Acesse sua conta GitHub e vá em _Settings_.
2. Dentro de Settings, vá em _Developer Settings_.
3. Ali dentro, três abas aparecem. Clique em _Personal access tokens > Tokens (classic)_.
4. Por fim, gere um token escolhendo obrigatoriamente uma data de expiração para ele - é possível que ele não expire, mas não é recomendado fazer essa escolha.

O access_token é necessário para que o projeto possa acessar informações privadas do GitHub. Ele
deve ficar em um arquivo '.env'.

**Conclusão**:

Este projeto é uma ferramenta de extração de informações no GitHub através de API. Ele é capaz de obter informações detalhadas sobre perfis e repositórios do GitHub e pode ser usado para diversos fins, como visualização de dados e análise de tendências.



**Sobre o projeto**:
O projeto foi inspirado no curso de _'Python e APIs: conhecendo a biblioteca Requests'_, ministrado pela professora Millena Gená e exibido na plataforma de ensino Alura. O projeto foi desenvolvido com o intuito de aprofundar os conhecimentos adquiridos no curso e de desenvolver uma ferramenta útil para extração de dados do GitHub. 

