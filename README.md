# POC - Transformação de Cenários de Teste em Script Automatizado

Este projeto é uma prova de conceito (POC) que utiliza IA para transformar cenários de teste escritos em linguagem natural em scripts de teste automatizados. O usuário pode escolher a ferramenta de automação desejada entre **Robot Framework**, **Selenium WebDriver** e **Cypress**, e a IA gera o script e, se necessário, uma massa de dados para execução do teste.

## Visão Geral

A aplicação é construída usando **Streamlit** para a interface de usuário e **LangChain** para o fluxo de prompts e comunicação com a API da OpenAI. A estrutura modular permite fácil escalabilidade e personalização.

## Estrutura do Projeto

```plaintext
project_root/
│
├── app.py                 # Arquivo principal da aplicação Streamlit
├── requirements.txt       # Lista de dependências do projeto
├── .env                   # Variáveis de ambiente (API Key da OpenAI)
│
├── config/
│   └── settings.py        # Configuração do LangChain e leitura da API Key
│
├── prompts/
│   └── templates.py       # Templates dos prompts usados para geração dos scripts
│
├── services/
│   ├── __init__.py        # Para tornar 'services' um pacote
│   └── generate_script.py # Função que usa LangChain para gerar o script de automação
│
├── utils/
│   └── helpers.py         # Funções auxiliares para o projeto
│
└── README.md              # Documentação do projeto
```

### Principais Componentes

- **app.py**: Interface da aplicação construída com Streamlit.
- **config/settings.py**: Configuração de variáveis de ambiente e inicialização da API da OpenAI.
- **prompts/templates.py**: Template dos prompts usados para geração dos scripts.
- **services/generate_script.py**: Lógica para geração dos scripts de automação usando LangChain.
- **.env**: Armazena a chave da API da OpenAI.

## Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com uma chave de API válida

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` e adicione sua chave de API da OpenAI:
   ```plaintext
   OPENAI_API_KEY="sua_api_key_aqui"
   ```

## Uso

1. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```
2. No navegador, insira os cenários de teste, escolha a ferramenta de automação e clique em "Gerar Script de Automação".
3. O script e a massa de dados (se necessário) serão exibidos.

## Exemplo de Entrada

Exemplo de cenário de teste que você pode inserir na aplicação:

```plaintext
Dado que o usuário está na página de login
Quando o usuário insere credenciais válidas
Então o usuário é redirecionado para a página inicial.
```

## Exemplo de Saída

Dependendo da ferramenta selecionada, a saída será o script automatizado correspondente, como Python para Selenium WebDriver, `.robot` para Robot Framework, ou JavaScript para Cypress.

## Personalização

- Para ajustar os templates de prompts, edite o arquivo `prompts/templates.py`.
- O arquivo `config/settings.py` gerencia as variáveis de ambiente e configuração do LangChain.

## Contribuição

Sinta-se à vontade para contribuir com melhorias e novos recursos. Crie um pull request ou abra uma issue.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

### Explicação

Este `README.md` fornece uma visão geral do projeto, incluindo a estrutura de diretórios, instruções de instalação e configuração, um guia de uso rápido, e informações sobre personalização. Ele deve ajudar tanto novos usuários quanto colaboradores a entenderem e configurarem rapidamente a POC.