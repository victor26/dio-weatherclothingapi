# Aplicação Flask com Docker e Azure Pipelines

## Visão Geral

Esta aplicação Flask fornece uma API simples que sugere roupas para o usuário com base na temperatura enviada. A API está conteinerizada usando Docker para fácil implantação e escalabilidade. Além disso, o repositório inclui configuração para integração contínua e entrega contínua (CI/CD) com Azure Pipelines, que automatiza a construção e implantação da imagem Docker no Azure Container Registry (ACR).

## Iniciando

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:
- Docker
- Python 3.9 ou superior

### Execução Local

Para executar a aplicação Flask localmente, siga estas etapas:

1. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

2. Inicie o servidor Flask:

    ```bash
    python app.py
    ```

A aplicação agora está rodando em `http://localhost:5000`.

### Dockerização

Para construir a imagem Docker localmente, execute:

```bash
docker build -t minha-aplicacao .
