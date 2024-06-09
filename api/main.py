from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from keras.preprocessing.image import img_to_array
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import mlflow
import time
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

mlflow.set_tracking_uri('file:///app/mlruns')
mlflow.set_experiment("Plant-Disease-API-Monitoramento")  # Nome do experimento

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("/app/models/Plant-Diseases-v2")

CLASS_NAMES = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Background_without_leaves', 'Blueberry___healthy', 'Cherry___Powdery_mildew', 'Cherry___healthy', 'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust', 'Corn___Northern_Leaf_Blight', 'Corn___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    with mlflow.start_run():
        start_time = time.time()

        image = read_file_as_image(await file.read())

        image = Image.fromarray(image)
        width, height = (128,128)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        img_batch = img_to_array(image)
        img_batch = np.expand_dims(img_batch, axis=0)  # Adiciona uma dimensão para batch
        img_batch = img_batch / 255.0  # Normalização se necessário

        predictions = MODEL.predict(img_batch)

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])

        end_time = time.time()
        latency = end_time - start_time

        # Registra métricas e logs no MLflow
        mlflow.log_metric("confidence", confidence)
        mlflow.log_metric("latency", latency) # Tempo de previsão

        probabilidade = int(float(confidence)*100)

        return {
            'Doença': predicted_class,
            'Probabilidade': f"{probabilidade}%"
        }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
