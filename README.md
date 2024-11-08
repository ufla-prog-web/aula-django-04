# Aula Django 04 - Sistema para Portal Biblioteca

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Aula-Python-brightgreen.svg" alt="Aula Python">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Aula-Django-blue.svg" alt="Aula Django">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Aula-Portal_Biblioteca-orange.svg" alt="Aula Portal Biblioteca">
  </a>
</p>

## Índice

* [Introdução](#introdução)
* [Recursos Utilizados](#recursos-utilizados)
* [Fundamentos Teóricos](#fundamentos-teóricos)
* [Objetivo da Aula](#objetivo-da-aula)
* [Desenvolvimento do Projeto](#desenvolvimento-do-projeto)
* [Próximas Etapas](#próximas-etapas)
* [Créditos e Referências](#créditos-e-referências)

## Introdução

<a href="#índice"><img align="right" width="15" height="15" src="./docs/up-arrow.png" alt="Voltar para topo"></a>

Aula Django 04. Projeto utilizando o Django para ser desenvolvido na Aula de GAC116 - Programação Web. Essa aula é uma continuação da Aula Django 03.

O objetivo desse projeto é criar um sistema para gestão de biblioteca.

Este tutorial foi elaborado baseado no tutorial disponível no [curso de django da w3schools](https://www.w3schools.com/django/index.php) e também baseado na [documentação oficial do django](https://docs.djangoproject.com/pt-br/5.0/).

A aula está estruturada em forma de tutorial, de forma que cada estudante vá replicando em seu computador os conceitos e recursos aqui mostrados. A aula mostra a evolução do código/solução para que os estudantes possa compreender como as diferentes tecnologias se conectam.

## Recursos Utilizados

<a href="#índice"><img align="right" width="15" height="15" src="./docs/up-arrow.png" alt="Voltar para topo"></a>

A seguir estão listados os principais recursos utilizados no desenvolvimento desta aula.

### Linguagens

* Python - Linguagem de Programação Principal
    * [link do site python](https://www.python.org/)
    * [link do curso da w3schools](https://www.w3schools.com/python/default.asp)
* HTML - Estrutura da Página Web
    * [link do curso da w3schools](https://www.w3schools.com/html/default.asp)
* CSS - Apresentação da Página Web
    * [link do curso da w3schools](https://www.w3schools.com/css/default.asp)
* JavaScript - Comportamento da Página Web
    * [link do curso da w3schools](https://www.w3schools.com/js/default.asp)
* SQL - Linguagem para Consultas no Banco de Dados
  * [link do curso da w3schools](https://www.w3schools.com/sql/default.asp)

### Framework

* Django - Framework Web
    * [link do site do django](https://www.djangoproject.com/)
    * [link do curso da w3schools](https://www.w3schools.com/django/index.php)
* Bootstrap - Framework CSS
    * [link do site do bootstrap](https://getbootstrap.com/)
    * [link do curso da w3schools](https://www.w3schools.com/bootstrap5/index.php)

### Bibliotecas

* Jinja - Biblioteca Python para Templates
    * [link do site do jinja](https://jinja.palletsprojects.com/en/3.1.x/)
* Chart.js - Biblioteca JavaScript para Gráficos
    * [link do site do chart.js](https://www.chartjs.org/)
* FontAwesome - Biblioteca CSS para Ícones
     * [link do site do fontawesome](https://fontawesome.com/)
* WhiteNoise - Biblioteca Python para Servir Arquivos Estáticos
    * [link do site do whitenoise](https://whitenoise.readthedocs.io/)
* Unfold - Biblioteca Python para Interface Administrativa do Django
    * [link do django-unfold](https://unfoldadmin.com/)

### Ferramentas

* Git - Sistema de Controle de Versão - [link](https://git-scm.com/)
* Github - Plataforma de Hospedagem de Códigos - [link](https://github.com/)
* Visual Studio Code - IDE - [link](https://code.visualstudio.com/)
* Pip - Gerenciador de Pacotes do Python - [link](https://pypi.org/project/pip/)
* Venv - Ambiente Virtual do Python - [link](https://docs.python.org/pt-br/3/library/venv.html)
* SQLite Online - SGBD - [link](https://sqliteonline.com/)
* DB Browser for SQLite - SGBD - [link](https://sqlitebrowser.org/)

## Fundamentos Teóricos

<a href="#índice"><img align="right" width="15" height="15" src="./docs/up-arrow.png" alt="Voltar para topo"></a>

A seguir estão destacados alguns dos principais fundamentos teóricos para entendimento desse tutorial.

### Características do Django

**1. Framework completo:** Django oferece tudo o que é necessário para o desenvolvimento de uma aplicação web, incluindo roteamento de URLs, mapeamento objeto-relacional (ORM), sistema de templates, autenticação, etc.

**2. Administração automática:** Com base nos modelos definidos, Django gera automaticamente uma interface administrativa poderosa e personalizável, economizando tempo no desenvolvimento de funcionalidades administrativas.

**3. ORM (Object-Relational Mapping):** O Django possui um ORM que facilita a interação com bancos de dados relacionais, permitindo que os desenvolvedores escrevam consultas em Python ao invés de SQL.

**4. Sistema de templates:** Django possui um sistema de templates eficiente que permite criar HTML dinâmico de forma organizada, utilizando lógica básica como laços e condicionais.

**5. Segurança embutida:** O Django se preocupa com a segurança, oferecendo proteção contra ataques comuns como SQL Injection, Cross-site Scripting (XSS), Cross-site Request Forgery (CSRF), e Clickjacking.

**6. Escalabilidade:** Django é altamente escalável, podendo lidar com grandes volumes de tráfego, como em sites populares que utilizam o framework (por exemplo, Instagram e Pinterest).

**7. Comunidade ativa e documentação:** Django conta com uma ampla comunidade de desenvolvedores e uma documentação completa e detalhada, facilitando a resolução de problemas e o aprendizado.

**8. Reutilização de código:** Django promove a reutilização de componentes por meio de pacotes chamados "apps". Cada app é modular e pode ser usado em diferentes projetos ou em diferentes partes da mesma aplicação.

**9. Suporte a várias bases de dados:** O Django suporta diferentes sistemas de banco de dados, como PostgreSQL, MySQL, SQLite e Oracle, tornando-o flexível para diversos ambientes.

**10. Testes integrados:** O Django tem suporte nativo para testes automatizados, permitindo que desenvolvedores escrevam e executem testes facilmente para garantir a qualidade do código.

### Arquitetura Web de Três Camadas

A arquitetura web de três camadas é um padrão de design de software que organiza uma aplicação em três níveis distintos, cada um com responsabilidades bem definidas. Essas camadas são:

**1. Camada de Apresentação (Frontend)**:

* Também chamada de interface de usuário, essa camada é responsável pela interação com o usuário. Ela inclui tudo o que o usuário vê e utiliza para interagir com o sistema, como páginas web, formulários, botões, e elementos visuais em geral.
* Aqui, são usados tecnologias como HTML, CSS, JavaScript e frameworks frontend (React, Angular, etc.).
* A camada de apresentação envia as entradas dos usuários para a camada de negócios e exibe os resultados de volta para o usuário.

**2. Camada de Negócios (Lógica da Aplicação - Backend)**:

* Nessa camada está a lógica de negócios da aplicação, ou seja, as regras que governam como os dados devem ser processados e as operações que devem ser realizadas. Ela trata os pedidos recebidos da camada de apresentação e executa as operações necessárias.
* Essa camada pode incluir validações, cálculos e chamadas ao banco de dados. Em termos de tecnologia, é geralmente desenvolvida com linguagens de programação como Python, Java, PHP, ou frameworks como Django, Spring Boot, Laravel, etc.

**3. Camada de Dados (Banco de Dados - Backend)**:

* A camada de dados gerencia o armazenamento e recuperação de dados em um banco de dados. Ela é responsável pela persistência dos dados e operações como criar, ler, atualizar e deletar (CRUD).
* Geralmente, são usados sistemas de gerenciamento de banco de dados relacionais (como MySQL, PostgreSQL) ou não relacionais (como MongoDB).
* A camada de negócios interage com essa camada para armazenar e buscar dados conforme necessário.

**Fluxo da Arquitetura de Três Camadas**:

* O usuário interage com a Camada de Apresentação.
* A Camada de Apresentação faz requisições para a Camada de Negócios.
* A Camada de Negócios processa a lógica e, se necessário, interage com a Camada de Dados.
* A Camada de Dados responde com os dados necessários para a Camada de Negócios.
* A Camada de Negócios retorna os resultados processados para a Camada de Apresentação.
* A Camada de Apresentação exibe os resultados para o usuário.

Essa separação facilita a manutenção e escalabilidade da aplicação, permitindo que cada camada possa ser modificada ou melhorada de forma independente.

![Arquitetura das Aplicações Web](./docs/arquitetura-web.png)

### Arquitetura MVT do Django

O modelo MVT (Model-View-Template) é uma arquitetura usada no framework Django para desenvolvimento de aplicações web. Ele organiza a aplicação em três componentes principais:

* **Model (Modelo)**: Responsável pela definição da estrutura dos dados e a interação com o banco de dados. Ele define as classes que representam as tabelas e seus relacionamentos, além de métodos para realizar consultas e operações nos dados.

* **View (Visão)**: Contém a lógica da aplicação. A view recebe as requisições dos usuários, processa os dados (geralmente acessando o Model), e retorna uma resposta, como uma página HTML renderizada ou dados em formato JSON.

* **Template (Apresentação)**: É a camada de apresentação, onde o conteúdo dinâmico gerado pela View é inserido em arquivos HTML. Os templates permitem a separação da lógica de negócio da interface de usuário, tornando o código mais organizado.

Diferente do padrão MVC, onde o controller gerencia a lógica de controle, no Django, a função das views cumpre esse papel, enquanto os templates gerenciam a apresentação.

A figura abaixo detalha os componentes descritos acima.

![Arquitetura MVT - Geral](./docs/mvt-1.png)

No modelo MVT do Django, as requisições seguem um fluxo bem definido, onde cada componente (Model, View, Template) desempenha um papel específico no processamento e resposta de uma requisição HTTP. O fluxo funciona da seguinte forma:

* **Recebimento da Requisição (HTTP Request)**: Quando um usuário acessa uma URL no navegador, o Django recebe a requisição HTTP correspondente. Esse processo começa no URL *dispatcher* (mapeador de URLs), que verifica qual view deve ser chamada com base na URL requisitada.

* **View (Visão)**: A View é o ponto de entrada para o processamento da requisição. A função ou classe associada à URL recebida é executada. Ela é responsável por: Receber a requisição do usuário; Executar a lógica necessária, que pode incluir validações, processamento de dados, ou interações com o banco de dados através dos Models; e Retornar uma resposta apropriada.

* **Model (Modelo)**: Se a View precisar acessar ou manipular dados, ela fará isso por meio do Model. O Model contém a lógica de negócios relacionada à persistência de dados, permitindo a View realizar operações como criar, ler, atualizar ou deletar registros no banco de dados.

* **Template (Apresentação)**: Após processar os dados, a View geralmente prepara um contexto (um dicionário de dados) e passa esse contexto para o Template. O Template é um arquivo HTML com marcações especiais do Django que permitem a inserção de dados dinâmicos. O Template renderiza esses dados em uma estrutura HTML, exibindo o conteúdo adequado com base nas informações passadas pela View.

* **Resposta (HTTP Response)**: Depois que o Template é renderizado, a View retorna uma resposta HTTP (normalmente uma página HTML ou dados JSON em APIs) ao navegador ou cliente. Essa resposta contém o conteúdo processado e visualizado pelo usuário.

A figura abaixo detalha o fluxo descrito acima.

![Arquitetura MVT - Requisição](./docs/mvt-2.png)

A figura abaixo detalha ainda mais a arquitetura MVT e as tecnologias envolvidas.

![Arquitetura MVT - Detalhes](./docs/mvt-3.png)

### Modelo ORM

O Django suporta o conceito de Mapeamento Objeto-Relacional (ORM). Através do ORM você define a modelagem de dados através de classes em Python. Com isso é possível gerar suas tabelas no banco de dados e manipulá-las sem necessidade de utilizar SQL (o que também é possível). Os registros de cada tabela são representados como instâncias das classes correspondentes.

## Objetivo da Aula

<a href="#índice"><img align="right" width="15" height="15" src="./docs/up-arrow.png" alt="Voltar para topo"></a>

A animação abaixo mostra de forma visual o resultado esperado nesta aula.

![Sistema Objetivo da Aula](./docs/objetivo.gif)

## Desenvolvimento do Projeto

<a href="#índice"><img align="right" width="15" height="15" src="./docs/up-arrow.png" alt="Voltar para topo"></a>

Os passos a seguir devem ser seguidos para alcançar o objetivo da aula.

### Clonando o Repositório

Inicialmente, clone o repositório da seguinte forma:

```bash
git clone https://github.com/ufla-prog-web/aula-django-04.git
```

### Baixando o Repositório

Caso deseje ao invês de clonar o repositório (método acima), baixe o repositório do [link](https://github.com/ufla-prog-web/aula-django-04) clicando em `Code` e `Download ZIP`.

### Abrindo o Visual Studio Code

Abra a IDE Visual Studio Code na pasta `aula-django-04`.

**Dica:** Abra o arquivo `README.md` e clique em `Open Preview to the Side` para facilitar a construção da aplicação.

**Dica:** Abra um terminal utilizando a IDE clicando em `Terminal` e `New Terminal`.

### Navegando até a Pasta do Projeto

Em seguida, navegue até a pasta do projeto (`portal_biblioteca`) dentro da pasta baixada do github (`aula-django-04`):

```bash
cd aula-django-04/
cd portal_biblioteca/
```

### Criando o Ambiente Virtual

Crie o ambiente virtual (venv) para isolar as instalações/dependências do Python:

Unix/macOS

```bash
python3 -m venv venv
```

Windows

```bash
py -m venv venv
```

**OBS:** no comando acima, o segundo nome `venv` é o nome que escolhemos para o nosso ambiente virtual (isso pode ser alterado).

### Ativando o Ambiente Virtual

Ative o ambiente virtual (venv) no seu computador utilizando o comando abaixo:

**Sistema Operacional:** Unix/Mac OS:

```bash
source venv/bin/activate
```

**Sistema Operacional:** Windows

```bash
Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\activate.bat
```

Quando desejar sair do ambiente virtual, basta digitar:

```bash
deactivate
```

### Fluxo de Trabalho no Django

A seguir é apresentado um fluxo de trabalho que pode ser seguido durante o desenvolvimento de um projeto utilizando o Django.

[![](https://mermaid.ink/img/pako:eNqN1E1y2yAUB_CrMHThTVLvveiMbcnfX9Nm0UTKgkrPDikCFZBTNxPfJaseoNMT-GJ9Qq5DNSyqlfjzAwF6wzPNVA60R7dCPWUPTFtyE6WS4NNPUjqVxjLBTj9Pv8GQFWRgzOlVc2ZSek-urz-QAaohBppstHoEq4hUJHpkcqeQNDMNnBxeZL8sA2roVJR0U9q3FRP8B9KOAWu53Jn35aGT0jQ948jhuIUL3Is40-5Zxk6Oaum-3n3zN1CUglkwb3rk9Dik-_pbxffKkNjY06vlmfLGjd24SWs9ew5PreVMHJyGPtCpdHvxU6dnrWlZXnDZOpCZk_P_O725w4sax98hq2xtMyUEZBZ_OO7N1wunl__qgn2Fgu80YiWNz5eOr1rcUfDdyrl14jNdSQN6D7pzKYu1YxtkfYnbMsg-gqmEZbmrtRXbww7ftRvRjNk0Bec3Ir8R-42R3xj7jYnfmNaTN8HnZP1F8x2zp1-aq3tyPB7JbdJdlxmeBRN_f95t3XGHecaM63Bbb_qMPQhAseVC9N6NooEfx-F4FI7H4XgSjqft2O-8u3RGfhyF41k4nofjRThehuOVH9MrWoAuGM_xonquWUrtAxSQ0h6-5rBlWA9YWvIFKaus-nSQGe1ZXcEVrcocKy_iDCuwoL0tEwZTyLlVetlcfu4OfPkDBV6NXw?type=png)](https://mermaid.live/edit#pako:eNqN1E1y2yAUB_CrMHThTVLvveiMbcnfX9Nm0UTKgkrPDikCFZBTNxPfJaseoNMT-GJ9Qq5DNSyqlfjzAwF6wzPNVA60R7dCPWUPTFtyE6WS4NNPUjqVxjLBTj9Pv8GQFWRgzOlVc2ZSek-urz-QAaohBppstHoEq4hUJHpkcqeQNDMNnBxeZL8sA2roVJR0U9q3FRP8B9KOAWu53Jn35aGT0jQ948jhuIUL3Is40-5Zxk6Oaum-3n3zN1CUglkwb3rk9Dik-_pbxffKkNjY06vlmfLGjd24SWs9ew5PreVMHJyGPtCpdHvxU6dnrWlZXnDZOpCZk_P_O725w4sax98hq2xtMyUEZBZ_OO7N1wunl__qgn2Fgu80YiWNz5eOr1rcUfDdyrl14jNdSQN6D7pzKYu1YxtkfYnbMsg-gqmEZbmrtRXbww7ftRvRjNk0Bec3Ir8R-42R3xj7jYnfmNaTN8HnZP1F8x2zp1-aq3tyPB7JbdJdlxmeBRN_f95t3XGHecaM63Bbb_qMPQhAseVC9N6NooEfx-F4FI7H4XgSjqft2O-8u3RGfhyF41k4nofjRThehuOVH9MrWoAuGM_xonquWUrtAxSQ0h6-5rBlWA9YWvIFKaus-nSQGe1ZXcEVrcocKy_iDCuwoL0tEwZTyLlVetlcfu4OfPkDBV6NXw)

### Instalando o Django

Instale o django dentro do ambiente virtual criado (testado na versão 5.0.3):

```bash
pip3 install django
```

ou

```bash
python -m pip install Django
```

Verifique a versão instalada do django (para ter certeza que tudo ocorreu bem):

```bash
django-admin --version
```

ou

```bash
python3 -m django --version
```

**OBS:** Caso o terminal não encontre o django-admin, execute o seguinte comando (utilizado geralmente quando não se utiliza o venv no laboratório DCC07):

```bash
export PATH=$PATH:~/.local/bin
```

### Instalando o WhiteNoise

Instale o WhiteNoise dentro do ambiente virtual:

```bash
pip3 install whitenoise
```

### Executando o Projeto

Antes de executar o projeto, execute o comando para fazer as migrações:

```bash
python3 manage.py migrate
```

Em seguida, execute comando abaixo para fazer a cópia dos arquivos estáticos:

```bash
python3 manage.py collectstatic
```

Inicie a execução do projeto django criado:

```bash
python3 manage.py runserver
```

**OBS:** Por padrão, o servidor de desenvolvimento escuta na porta 8000, mas você pode especificar uma porta diferente como argumento opcional, por exemplo, `python3 manage.py runserver 8081`.

Acesse através do navegdor web a página [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

A aula anterior avançou até aqui.

### Mudando o Tema do Ambiente Administrativo para Unfold

Nesta etapa, iremos mudar o tema do ambiente adminstrativo padrão para o Unfold que é um ambiente mais moderno, robusto e visualmente atraente.

Para isso, instale o unfold do django utilizando o comando abaixo:

```bash
pip3 install django-unfold
```

Em seguida, inclua o unfold na variável `INSTALLED_APPS` em `settings.py` conforme abaixo:

```python
...
INSTALLED_APPS = [
    'unfold', # incluir para usar o tema unfold 
    'django.contrib.admin',
    ...
]
...
```

Em seguida, execute o comando:

```bash
python3 manage.py collectstatic
```

Em seguida, execute a aplicação:

```bash
python3 manage.py runserver
```

Para mais informações sobre o Unfold consulte o [link](https://unfoldadmin.com/docs/installation/quickstart/).

### Incluindo Busca nas Tabelas do Ambiente Adminstrativo

Nessa etapa, iremos criar um campo de busca dentro do ambiente administrativo para filtrar dados. Esse recurso é mais adequado para campos de texto, mas pode ser usado em números também como ano.

Para isso, atualize o código do `admin.py` conforme o exemplo abaixo.

```python
...
class LivroAdmin(admin.ModelAdmin):
    list_display = ("nome", "autor", "ano")
    search_fields = ("nome", "autor") # campo de busca

class TCCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "orientador", "ano")
    search_fields = ("titulo", "autor", "orientador") # campo de busca
...
```

Em seguida, execute a aplicação:

```bash
python3 manage.py runserver
```

Em seguida, entre no ambiente adminstrativo [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e então realize buscas nas tabelas Livro e TCC.

### Incluindo Filtros nas Tabelas do Ambiente Adminstrativo

Nessa etapa, iremos criar um filtro dentro do ambiente administrativo para filtrar dados. Esse filtro é adicionado na barra lateral, permitindo filtrar itens com base em determinados campos. Ideal para campos com valores repetitivos, como `status` ou `categoria`.

Para isso, atualize o código do `admin.py` conforme o exemplo abaixo.

```python
...
class LivroAdmin(admin.ModelAdmin):
    list_display = ("nome", "autor", "ano")
    search_fields = ("nome", "autor")
    list_filter = ("autor", "ano") # campos para filtro

class TCCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "orientador", "ano")
    search_fields = ("titulo", "autor", "orientador")
    list_filter = ("autor", "orientador", "ano") # campos para filtro
...
```

Em seguida, execute a aplicação:

```bash
python3 manage.py runserver
```

Em seguida, entre no ambiente adminstrativo [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e então realize filtros nas tabelas Livro e TCC.

### Incluindo Outros Detalhes no Admin.py

Nesta etapa, iremos incluir mais alguns detalhes para personalização do ambiente de administração do Django. O primeiro detalhe incluso é uma ordenação padrão dos registros ao serem exibidos na interface de administração. O segundo detalhe incluso é permitir que determinados campos sejam editados diretamente na lista de itens. Por fim, alguns detalhes foram inclusos de customização do título e cabeçalho da interface de administração.

Assim, inclua as seguintes modificações no arquivo `admin.py`:

```python
...
class TCCAdmin(admin.ModelAdmin):
    ...
    ordering = ('autor',)    # para ordenação inicial dos dados
    list_editable = ('ano',) # para edição dos campos diretamente na lista de itens
...
admin.site.site_header = "Administração da Biblioteca"
admin.site.index_title = "Bem-vindo a Administração do Portal Biblioteca"
```

Em seguida, execute a aplicação:

```bash
python3 manage.py runserver
```

Agora, acesse o ambiente administrativo e analise as modificações realizadas.

### Incluindo Testes Unitários no Django

Nesta etapa, iremos incluir testes de software no Django. O Django oferece uma estrutura robusta com o módulo `django.test`. Essa estrutura permite criar testes para verificar o comportamento de sua aplicação, ajudando a assegurar que as funcionalidades implementadas funcionam conforme esperado. 

O Django utiliza o módulo unittest do Python, que permite a criação de classes de teste. Por padrão, o Django criará um banco de dados temporário para os testes, garantindo que o banco de dados principal não seja afetado.

Em Django, os testes geralmente são colocados no arquivo `tests.py` dentro de cada aplicativo (app). A estrutura básica para criar um teste em Django é a seguinte:

1. Importar TestCase do módulo `django.test`.
2. Criar uma classe de teste que herda de `TestCase`.
3. Escrever métodos de teste dentro dessa classe. Cada método deve começar com `test_`.

Escreva o código a seguir no arquivo `tests.py` da pasta `biblioteca`.

```python
from django.test import TestCase
from .models import Livro
from .models import TCC

class ModeloTestCase(TestCase):
    def setUp(self):
        Livro.objects.create(nome="Introdução ao Django", autor="João Silva", ano=2024)
        TCC.objects.create(titulo="Análise de Sistemas Web", autor="José Carvalho", orientador="Prof. Carlos Souza", ano=2023)

    def test_criacao_e_conteudo_livro(self):
        livro = Livro.objects.get(nome="Introdução ao Django")
        self.assertEqual(livro.autor, "João Silva")
        self.assertEqual(livro.ano, 2024)

    def test_criacao_e_conteudo_tcc(self):
        tcc = TCC.objects.get(titulo="Análise de Sistemas Web")
        self.assertEqual(tcc.autor, "José Carvalho")
        self.assertEqual(tcc.orientador, "Prof. Carlos Souza")
        self.assertEqual(tcc.ano, 2023)
```

**Explicação**: 
* `setUp`: Esse método é executado antes de cada teste e é útil para configurar dados de teste, como a criação de objetos no banco de dados.
* **Método de Teste**: Cada método de teste deve começar com `test_` e testar uma funcionalidade específica. Nesse exemplo, o método `test_criacao_e_conteudo_livro` verifica se o livro foi criado com o autor e ano correto.
* **Assertions**: `self.assertEqual` é uma das muitas "assertions" disponíveis para verificar condições nos testes. Outras comuns incluem `self.assertTrue`, `self.assertFalse`, `self.assertIn`, entre outras.

Em seguida, execute o teste:

```bash
python manage.py test
```

Para testar uma view (por exemplo, uma página de detalhe de um TCC), o Django permite simular requisições HTTP usando o cliente de teste (`self.client`). Inclua as seguintes modificações no código do arquivo `tests.py`:

```python
...
from django.urls import reverse
...
class ViewTCCTestCase(TestCase):
    def setUp(self):
        self.tcc = TCC.objects.create(titulo="Análise de Interfaces Web", autor="Cesar Silva", orientador="Prof. Ricardo Souza", ano=2022)

    def test_view_tcc_detalhes(self):
        url = reverse("tcc_detalhes", args=[self.tcc.id])
        response = self.client.get(url)
        #print(url)
        #print(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Análise de Interfaces Web")
```

**Explicação**: Neste exemplo, o teste verifica se a página de detalhes do TCC é acessada corretamente e contém o título do TCC. O comando `reverse` é utilizado para resolver o caminho de uma URL com base no nome dado a ela no arquivo de configuração de URLs (`urls.py`).

Em seguida, execute o teste:

```bash
python manage.py test
```

### Configurando o Fuso Horário do Brasil

Nesse etapa, iremos configurar o fuso horário padrão da aplicação para o fuso horário de São Paulo (mesmo utilizado em MG).

Para isso, realize a seguinte atualização na variável `TIME_ZONE` em `settings.py` conforme abaixo:

```python
...
TIME_ZONE = 'America/Sao_Paulo'
...
```

**Explicação**: O atributo `TIME_ZONE` especifica em qual fuso horário o Django deve armazenar e manipular dados de data e hora no banco de dados, além de exibir essas informações nas views e na interface de administração. Nesse [link](https://github.com/guilhermeonrails/language_code_django/blob/tz_list/list.py) tem uma lista com as opções disponíveis de fuso horário.

Em seguida, execute o servidor, faça uma atualização qualquer no modelo via ambiente adminstrativo e veja as informações relativas as mudanças nas informações de "Ações recentes" do ambiente adminstrativo.

Para mais informações sobre as configurações disponíveis no arquivo de settings, consulte o [link](https://docs.djangoproject.com/en/5.1/ref/settings/).

### Adicionando Controle de Usuários no Django

Esta parte do tutorial foi baseada na [documentação oficial django](https://docs.djangoproject.com/pt-br/5.0/topics/auth/default/) e também na [videoaula](https://www.youtube.com/watch?v=gdhiA6wObw0).

O Django possui já prontos diversos recursos para trabalhar com autenticação de usuários e controle de nível de acesso.

Agora, iremos adicionar em nosso projeto um sistema de gestão de usuários. Para criarmos na sequência as telas de login e cadastro na plataforma.

Para isso, iremos criar uma outra aplicação/aplicativo web dentro do nosso projeto. Assim, digite o seguinte conteúdo.

```bash
python3 manage.py startapp usuarios
```

Agora, atualize a lista `INSTALLED_APPS` em `settings.py` na pasta `portal_biblioteca`:

```python
...
INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'biblioteca',
    'usuarios', #adicone seu app aqui 
]
...
```

Agora, iremos criar uma pasta chamada `templates` dentro da aplicação `usuarios`. Nesta pasta, iremos criar um arquivo chamado `login.html` com o seguinte conteúdo:

```html
<h1>Login</h1>
```

Ainda nesta pasta, iremos criar também um arquivo chamado `cadastro.html` com o seguinte conteúdo:

```html
<h1>Cadastro</h1>
```

Em seguida, precisamos definir as views do nosso sistema de login e cadastro. Assim, digite o código abaixo no arquivo `views.py` na pasta `usuarios`:

```python
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')
```

Agora, crie na pasta `usuarios` um arquivo chamado `urls.py` com o seguinte conteúdo:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
]
```

Agora, precisamos informar a nossa aplicação principal da existência dessas novas URLs. Assim, edite o código `urls.py` da pasta `porta_biblioteca` da seguinte forma:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('biblioteca.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),   #adicione essa linha aqui
]
```

Agora, reinicie o servidor:

```bash
python3 manage.py runserver
```

Por fim, acesse o endereço [127.0.0.1:8000/](127.0.0.1:8000/). Navegue pelas abas Login e Cadastre-se.

### Melhorando a Tela de Cadastro

Agora, iremos melhorar a exibição da tela de Cadastro.

Assim, no arquivo `cadastro.html` digite o seguinte:

```html
{% extends "base.html" %}

{% block titulo %}
    Portal Biblioteca - Cadastro de Usuário
{% endblock %}

{% block conteudo %}
    <main class="container mt-5">
        <center>
            <h1>Cadastre-se</h1>            
            <form action="{% url 'cadastro' %}" method="POST" onsubmit="return validaSenha()">
                {% csrf_token %}
                <div class="input-group">
                    <span class="input-group-text">Usuário: </span>
                    <input type="text" class="form-control" placeholder="Usuário ..." name="usuario" required>
                </div>
                <br>
                <div class="input-group">
                    <span class="input-group-text">E-mail: </span>
                    <input type="email" class="form-control" placeholder="E-mail ..." name="email" required>
                </div>
                <br>
                <div class="input-group">
                    <span class="input-group-text">Senha: </span>
                    <input type="password" class="form-control" placeholder="Senha ..." id="password" name="senha" required>
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="button" onclick="alterarVisibilidadeSenha('password')">
                            <i class="fa fa-eye"></i>
                        </button>
                    </div>
                </div>
                <br>
                <div class="input-group">
                    <span class="input-group-text">Repetir Senha: </span>
                    <input type="password" class="form-control" placeholder="Repetir Senha ..." id="confirm_password" name="confirma_senha" required>
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="button" onclick="alterarVisibilidadeSenha('confirm_password')">
                            <i class="fa fa-eye"></i>
                        </button>
                    </div>
                </div>
                <br>
                <div id="passwordError" class="alert alert-danger" style="display: none;">
                    As senhas não coincidem.
                </div>
                <br>
                <button type="submit" class="btn btn-primary">Cadastrar</button>
            </form>
        </center>
    </main>
    <script>
        function alterarVisibilidadeSenha(fieldId) {
            const field = document.getElementById(fieldId);
            if (field.type === "password") {
                field.type = "text";
            } else {
                field.type = "password";
            }
        }
        function validaSenha() {
            const password = document.getElementById("password").value;
            const confirmPassword = document.getElementById("confirm_password").value;
            const errorDiv = document.getElementById("passwordError");

            if (password !== confirmPassword) {
                errorDiv.style.display = "block";
                return false; // Impede o envio do formulário
            } else {
                errorDiv.style.display = "none";
                return true; // Permite o envio do formulário
            }
        }
    </script>
{% endblock %}
```

**Explicação:** O código acima cria um formulário com os seguintes campos: usuário, email, senha, repetir senha e botão cadastrar. Neste formulário, quando clicado no botão "Cadastrar" enviará uma ação via método POST para a url de nome `cadastro` (nome definido no arquivo `url.py`). A tag `csrf_token` é necessária para fazer uma verificação de segurança.

**Explicação:** O CSRF Token, que significa "Cross-Site Request Forgery Token" (Token de Proteção contra Solicitação Falsificada entre Sites), é uma medida de segurança utilizada em aplicações da web para proteger contra ataques CSRF (Cross-Site Request Forgery), também conhecidos como ataques de falsificação de solicitação entre sites. Um ataque CSRF ocorre quando um invasor engana um usuário autenticado a executar ações indesejadas em um site sem o conhecimento ou consentimento do usuário. Isso é feito explorando o fato de que os navegadores da web geralmente incluem automaticamente cookies de sessão em todas as solicitações para um domínio, incluindo solicitações maliciosas.

Em seguida, atualize o código do método cadastro na `view.py`.

```python
from django.http import HttpResponse
...
def cadastro(request): # atualize essa função
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else: #senão será via método "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        return HttpResponse(usuario)
```

Em seguida, acesse o endereço [http://127.0.0.1:8000/auth/cadastro](http://127.0.0.1:8000/auth/cadastro) e efetue um cadastro e analise o resultado na tela.

Até aqui, não efetuamos de fato um cadastro, apenas exibimos na tela a informação do usuário.

Agora, iremos inserir as informações cadastradas no BD.

Assim, atualize o código do método `cadastro` na `view.py`.

```python
# faça essas inclusões
from django.contrib.auth.models import User
from django.contrib import messages
...
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else: #senão será via método "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se o usuário já está cadastrado
        user = User.objects.filter(username=usuario).first()
        if user:
            messages.error(request, 'Já existe um usuário com esse nome. Tente novamente.')
            return render(request, 'cadastro.html')

        # Cria e salva o usuário
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()
        
        return render(request, 'login.html')
```


Por fim, altere também o código do `cadastro.html` para exibir as mensagens de feedback, conforme código abaixo:

```html
...
        </form>
        <!-- Exibe mensagens de erro ou sucesso -->
        <br>
        {% if messages %}
            {% for message in messages %}
                <div class="alert {% if message.tags == 'success' %}alert-success{% else %}alert-danger{% endif %}" role="alert">
                    {{ message }}
                </div>
            {% endfor %}
        {% endif %}
        <!-- Fim do trecho que exibe mensagens -->
    </center>
</main>
...
```

Em seguida, acesse o endereço [http://127.0.0.1:8000/auth/cadastro](http://127.0.0.1:8000/auth/cadastro) e efetue um cadastro e analise o resultado na tela e também no menu administrativo do Django. Efetue também cadastro de dois usuários com mesmo email e analise o resultado.

**OBS:** O Django não armazena senhas brutas (texto não criptografado) no modelo de usuário. Ele armazena apenas um hash da senha.

Para mais detalhes sobre a classe `User`, consulte a [documentação oficial](https://docs.djangoproject.com/pt-br/5.0/topics/auth/default/).

### Melhorando a Tela de Login

Agora, iremos melhorar a exibição da tela de Login.

Assim, atualize o código do arquivo `login.html` para o seguinte:

```html
{% extends "base.html" %}

{% block titulo %}
    Portal Biblioteca - Login
{% endblock %}

{% block conteudo %}
    <main class="container mt-5">
        <center>
            <h1>Login</h1>
            <form action="{% url 'login' %}" method="POST">
                {% csrf_token %}
                <div class="input-group">
                    <span class="input-group-text">Usuário: </span>
                    <input type="text" class="form-control" placeholder="Usuário ..." name="usuario" required>
                </div>
                <br>
                <div class="input-group">
                    <span class="input-group-text">Senha: </span>
                    <input type="password" class="form-control" placeholder="Senha ..." id="password" name="senha" required>
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="button" onclick="alterarVisibilidadeSenha('password')">
                            <i class="fa fa-eye"></i>
                        </button>
                    </div>
                </div>
                <br>
                <input type="submit" value="Logar" class="btn btn-primary">
            </form>
            <br>
            {% if messages %}
                {% for message in messages %}
                    <div class="alert {% if message.tags == 'success' %}alert-success{% else %}alert-danger{% endif %}" role="alert">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        </center>
    </main>
    <script>
        function alterarVisibilidadeSenha(fieldId) {
            const field = document.getElementById(fieldId);
            if (field.type === "password") {
                field.type = "text";
            } else {
                field.type = "password";
            }
        }
    </script>
{% endblock %}
```

Em seguida, atualize o código do método `login` na `view.py`.

```python
# adicione essas importações
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
...
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)
        if user:
            login_django(request, user)
            return render(request, 'principal.html')
        else:
            messages.error(request, 'Usuário ou senha inválidos. Tente novamente.')
            return render(request, 'login.html')
```

Em seguida, acesse o endereço [http://127.0.0.1:8000/auth/login](http://127.0.0.1:8000/auth/login) e  efetue um login e analise o resultado na tela. Tente colocar um usuário válido e um usuário inválido.

**Explicação:** As principais diferenças entre "authenticate" e "login" do django são destacadas a seguir:

**authenticate:**
* O método "authenticate" é uma função fornecida pelo Django que é usada para verificar as credenciais de um usuário em um sistema de autenticação.
* Ele recebe as informações de login do usuário, como nome de usuário e senha, e verifica se essas informações correspondem a um usuário registrado no sistema.
* Se as credenciais estiverem corretas, o método "authenticate" retornará um objeto de usuário válido que representa o usuário autenticado. Caso contrário, retornará "None".

**login:**
* O método "login" refere-se ao processo de estabelecer uma sessão de usuário autenticada em um aplicativo da web após a autenticação bem-sucedida.
* O Django fornece uma função chamada "login" que permite que você associe um objeto de usuário autenticado a uma sessão. Isso é importante para manter o estado de autenticação do usuário durante a sessão.
* A função "login" normalmente é usada após o usuário ser autenticado com sucesso usando o "authenticate".

### Exibindo Informações na Navbar do Usuário Logado

Nesta etapa, iremos colocar algumas informações na navbar sobre o usuário que está logado no sistema. 

Para isso, atualize o código o código `base.html`, conforme código abaixo:

```html
...
    <div>
        ...
        <li class="nav-item">
            <a class="nav-link active" href="/admin"><i class="fa-solid fa-lock"></i> Admin</a>
        </li>
    </ul>
    <!-- Trecho inserido no HTML -->
    <ul class="navbar-nav ms-auto">
        {% if user.is_authenticated %}
            <li class="nav-item">
                <a class="nav-link active" href="#"><b>Usuário:</b> {{ user.username }}</a>
            </li>
            <a class="navbar-brand" href="#">
                <img src="{% static 'img_avatar.png' %}" alt="Avatar" style="width:36px;" class="rounded-pill">
            </a>
        {% endif %}
    </ul>
    <!-- Fim do trecho inserido no HTML -->
</div>
```

Em seguida, é necessário copiar o arquivo `img_avatar.png` da pasta `docs` para a pasta `staticfiles`.

Em seguida, execute o comando abaixo:

```bash
python3 manage.py collectstatic
```

Em seguida, reinicie o servidor:

```bash
python3 manage.py runserver
```

Por fim, acesse o endereço [http://127.0.0.1:8000](http://127.0.0.1:8000) e analise a nova navbar com informações do usuário logado no sistema.

Repare que a tela principal não está ficando com a configuração do usuário logado. Para resolver isso modifique a view principal no arquivo `views.py` na pasta `biblioteca`.

```python
...
def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render({}, request)) # linha atualizada
...
```

Execute o programa e analise o resultado.

### Adicionando Logout no Sistema

Agora, iremos adicionar no nosso sistema o recurso de logout.

Para isso, vá no arquivo `views.py` da pasta `usuarios` e adicione o seguinte conteúdo:

```python
from django.contrib.auth import logout as logout_django
...

def logout(request):
    logout_django(request)
    return render(request, 'login.html')
```

**Explicação:** Quando você chama `logout()` do django ou `logout_django()` neste caso, os dados da sessão da solicitação atual são completamente limpos. Todos os dados existentes são removidos. Isso evita que outra pessoa use o mesmo navegador para fazer login e ter acesso aos dados da sessão do usuário anterior.

Em seguida, vá no arquivo `urls.py` da pasta `usuarios` e adicione a seguinte rota.

```python
...
    path('logout', views.logout, name='logout'),
...
```

Por fim, acesse o endereço [http://127.0.0.1:8000](http://127.0.0.1:8000). Faça logout e login e analise a navbar.

### Disponibilizando o Dashboard Apenas para Usuários Logados

Agora, iremos permitir que a visualização dos dashboards esteja disponível apenas se o usuário estiver logado na plataforma.

Dessa maneira, atualize o código da função dashboard em `view.py` da pasta `biblioteca` para o seguinte:

```python
...
def dashboard(request):
    if request.user.is_authenticated:
        qtd = QuantitativoMateriais.objects.all().values()
        template = loader.get_template('dashboard.html')
        v = qtd[0]
        context = {
            'labels': ['Livros', 'TCCs', 'Dissertações', 'Teses', 'Apostilas', 'Jornais'],
            'data': [v['livros'], v['tccs'], v['dissertacoes'], v['teses'], v['apostilas'], v['jornais']]
        }
        return HttpResponse(template.render(context, request))
    return HttpResponse("Você precisa estar logado!")
```

Em seguida, abra uma guia anônima do navegador e acesse o endereço [http://127.0.0.1:8000](http://127.0.0.1:8000). Tente acessar a tela de dashboard. Na sequência, faça login na plataforma e então tente acessar o dashboard.

Uma outra forma de fazer a mesma operação é utilizando o decorador `login_required`. Atualize o seu código da função dashborad em `view.py` da pasta `biblioteca` para o seguinte:

```python
from django.contrib.auth.decorators import login_required
...
@login_required(login_url="/auth/login")
def dashboard(request):
    qtd = QuantitativoMateriais.objects.all().values()
    template = loader.get_template('dashboard.html')
    v = qtd[0]
    context = {
        'labels': ['Livros', 'TCCs', 'Dissertações', 'Teses', 'Apostilas', 'Jornais'],
        'data': [v['livros'], v['tccs'], v['dissertacoes'], v['teses'], v['apostilas'], v['jornais']]
    }
    return HttpResponse(template.render(context, request))
```

Em seguida, abra uma guia anônima do navegador e acesse o endereço [http://127.0.0.1:8000](http://127.0.0.1:8000). Tente acessar a tela de dashboard. Perceba que portal redireciona para a tela de login, isso ocorre, pois colocamos isso no parâmetro `login_url`. Na sequência, faça login na plataforma e então tente acessar o dashboard.

## Próximas Etapas

<a href="#índice"><img align="right" width="15" height="15" src="./docs/up-arrow.png" alt="Voltar para topo"></a>

Agora que você sabe como construir uma página web completa utilizando o framework Django, utilize os conhecimentos e exemplos aqui apresentados para fazer o seu trabalho final de implementação.

## Créditos e Referências

<a href="#índice"><img align="right" width="15" height="15" src="./docs/up-arrow.png" alt="Voltar para topo"></a>

Este tutorial foi inspirado nos seguintes recursos:

* [Documentação oficial do django](https://docs.djangoproject.com/pt-br/5.0/)
* [Curso de Django da w3schools](https://www.w3schools.com/django/index.php)
