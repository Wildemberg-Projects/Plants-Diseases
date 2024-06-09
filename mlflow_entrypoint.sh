#!/bin/bash

export MLFLOW_TRACKING_URI=file:///app/mlruns

# Iniciar o servidor MLflow em background
mlflow ui --host 0.0.0.0 --port 5000 &

# Iniciar o servidor Uvicorn para FastAPI
uvicorn api.main:app --host 0.0.0.0 --port 8000
