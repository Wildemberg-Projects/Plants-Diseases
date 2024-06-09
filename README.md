# Plants-Diseases
Repositório destinado a criação de um modelo de aprendizado de máquina para identificação de doenças em plantas.

## Sobre o Projeto
Tendo em vista a importância de identificar doenças e problemas em plantios com antecedência, buscando minimizar os danos causados, nossa equipe embarcou no projeto "Plant Disease", que consiste no desenvolvimento de um modelo Machine Learning o qual realiza o processamento de imagens de folhas e plantas, a fim de identificação de doenças como ferrugem, oídio e outras, trazendo o grande benefício do tempo para grandes e pequenos agricultores.

## Como executar o projeto de Treinamento
Para execução do arquivo .ipynb, é nessário abrí-lo no ambiente [Colab da Google](https://colab.research.google.com/github/Wildemberg-Projects/Plants-Diseases/blob/main/main.ipynb) para garantia do bom funcionamento dos scripts.  

## Como executar a api
* Entre na pasta raiz pelo terminal
* Execute os comandos:
~~~~bash
docker build -t plants-diseases-api .
docker run -d --name plants-diseases-api-container -p 8000:8000 -p 5000:5000 plants-diseases-api
~~~~
* A api irá rodar na porta 8000;

Após abrir o arquivo no ambiente, execute a célula de instalação das depêndencias. Feito isso, o ambiente está configurado e pronto para prosseguir a execução das outras células para carregamento dos dados e gráficos.  

**OBS:** Caso opte por executar em um ambiente local, retire os comentários nos comandos de instalação de depências da primeira célula, para que seja instalado tudo que é necessário.
