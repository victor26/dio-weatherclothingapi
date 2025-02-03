# Usa a imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências e instala as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos da aplicação para o diretório de trabalho
COPY . .

# Informa ao Docker a porta que a aplicação escuta
EXPOSE 5000

# Executa a aplicação Flask quando o contêiner inicia
CMD ["flask", "run", "--host=0.0.0.0"]
