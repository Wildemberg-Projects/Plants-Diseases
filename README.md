# Plants-Diseases
Repositório destinado a criação de um modelo de aprendizado de máquina para identificação de doenças em plantas.

# URL do deploy
[Link para a API Pública](https://plants-diseases-api-ytito7x2pa-uc.a.run.app/docs)

## Sobre o Projeto
Tendo em vista a importância de identificar doenças e problemas em plantios com antecedência, buscando minimizar os danos causados, nossa equipe embarcou no projeto "Plant Disease", que consiste no desenvolvimento de um modelo Machine Learning o qual realiza o processamento de imagens de folhas e plantas, a fim de identificação de doenças como ferrugem, oídio e outras, trazendo o grande benefício do tempo para grandes e pequenos agricultores.

## Como executar o projeto de Treinamento
Para execução do arquivo .ipynb, é nessário abrí-lo no ambiente [Colab da Google](https://colab.research.google.com/github/Wildemberg-Projects/Plants-Diseases/blob/main/main.ipynb) para garantia do bom funcionamento dos scripts.  

## Como executar a api
* Entre na pasta raiz pelo terminal
* Execute os comandos:
~~~~bash
docker build -t plants-diseases-api .
docker run -d --name plants-diseases-api-container -p 8080:8080 -p 5000:5000 plants-diseases-api
~~~~
* A api irá rodar na porta 8000 e o mlflow na 5000;

Após abrir o arquivo no ambiente, execute a célula de instalação das depêndencias. Feito isso, o ambiente está configurado e pronto para prosseguir a execução das outras células para carregamento dos dados e gráficos.  

**OBS:** Caso opte por executar em um ambiente local, retire os comentários nos comandos de instalação de depências da primeira célula, para que seja instalado tudo que é necessário.

## Deploy

* Se logue pela cli da google cloud e coloque o projeto em qual vai trabalhar
~~~~bash
gcloud auth login
gcloud config set project PROJECT_ID
~~~~
* Ative os plugins de:
    * artifact Registry
    * Cloud build
    * cloud deploy
* Criando um artifact: 
~~~~bash
gcloud artifacts repositories create NOME_DA_PASTA --repository-format=docker --location=us-central1 --description="descrição do artifact"

#gcloud artifacts repositories create plants-diseases-v2 --repository-format=docker --location=us-central1 --description="api e mlflow da IA plants diseases"
~~~~
* criando imagem e enviando:
~~~~bash
gcloud builds submit --region=us-central1 --tag CAMINHO_DO_ARQUIVO_NO_GC/NOME_DA_IMAGEM:TAG

#gcloud builds submit --region=us-central1 --tag us-central1-docker.pkg.dev/plants-diseases-425912/plants-diseases-v2/plants-diseases-api:tag1
~~~~
* Realizando deploy:
~~~~bash
gcloud run deploy --image=CAMINHO_DA_IMAGEM_NO_GC:TAG_DEFINIDA

#gcloud run deploy --image=us-central1-docker.pkg.dev/plants-diseases-425912/plants-diseases-v2/plants-diseases-api:tag1
~~~~
