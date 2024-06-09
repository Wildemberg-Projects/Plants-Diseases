#!/bin/bash

# Inicie o MLflow em segundo plano
mlflow server --backend-store-uri file:///app/mlruns --default-artifact-root /app/mlruns --host 0.0.0.0 --port 5000 &

# Aguarde um curto período para garantir que o MLflow tenha tempo para iniciar
sleep 5

# Inicie o FastAPI na porta 8080
uvicorn api.main:app --host 0.0.0.0 --port 8080
