# Use uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY api ./api
COPY models ./models
COPY mlflow_entrypoint.sh .

# Criar o diretório de armazenamento do MLflow
RUN mkdir -p /app/mlruns

# Exponha as portas onde a aplicação e o MLflow irão rodar
EXPOSE 8000
EXPOSE 5000

# Comando para iniciar a aplicação e o MLflow
CMD ["./mlflow_entrypoint.sh"]
