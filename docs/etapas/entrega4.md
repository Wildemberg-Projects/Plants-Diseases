# Preparação dos dados

## Divisão dos conjuntos de dados

Com a finalidade de alcançar uma melhor organização ao utilizar o modelo, foi realizada a divisão de um conjunto de dados (ds) em conjuntos de treinamento, validação e teste, como demonstrado na Imagem 1. Inicialmente, define-se que 80% dos dados serão destinados ao conjunto de treinamento. Em seguida, a variável ‘train_size’ é calculada como o número inteiro do tamanho total do conjunto de dados multiplicado pela proporção destinada ao treinamento. Após a definição do tamanho do conjunto de treinamento, os dados são aleatoriamente embaralhados. O próximo passo é atribuir os dados de treinamento, utilizando o método take, que seleciona os primeiros ‘train_size’ elementos do conjunto de dados embaralhados. Em seguida, os dados restantes após o conjunto de treinamento são usados para formar o conjunto de teste. Esses dados são divididos ao meio, onde metade é destinada ao conjunto de validação e a outra metade ao conjunto de teste. Essa abordagem permite avaliar o desempenho do modelo em dados não vistos durante o treinamento, contribuindo para uma avaliação mais precisa da generalização do modelo.

<center>

![alt text](/assets/RepartTrenio.png)

Imagem 1: Repartição de treino, validação e teste(Autor, 2024)
</center>

<br>

## Qualidade da limpeza dos dados

O conjunto de dados selecionado foi tratado com técnicas de data augmentation e já inclui imagens pré-processadas e bem tratadas no que diz respeito à direção, iluminação e clareza das imagens, não demandando um tratamento profundo (Imagem 2). Essas técnicas de augmentation contribuem para melhorar a capacidade do modelo de generalizar para novas imagens e garantir sua eficácia em diferentes contextos e condições.
 
<center>

![alt text](/assets/ExempDataset.png)

Imagem 2: Exemplos de imagens do Dataset (Autor, 2024)
</center>

<br>

Pelo alto custo de RAM que dificultaria o processamento dos moSdelos de Machine Learning e com o objetivo de simplificar o tratamento do banco de imagens, foi utilizado um cache de imagens, permitindo uma maior disponibilidade, além da randomização e pré-carregamento dos dados (Imagem 3).

<center>

![alt text](/assets/Cacheamento.png)

Imagem 2: Cacheamento, randomização e pré-carregamento dos dados (Autor, 2024)
</center>

<br>

## Normalização e padronização

A normalização de dados é essencial no processamento de imagens e em outras tarefas de aprendizado de máquina, pois ajusta a escala dos valores para um intervalo específico, geralmente entre 0 e 1. A normalização ajuda a evitar problemas de convergência durante o treinamento, permitindo que os modelos aprendam de forma mais eficiente com os dados, uma vez que todas as características estejam na mesma ordem de grandeza. No trecho de código mostrado na Imagem 4, primeiramente, é criado um modelo sequencial que irá aplicar uma série de transformações às imagens. A primeira transformação é a “Resizing”, que ajusta o tamanho das imagens para um tamanho padrão definido pela variável ‘IMAGE_SIZE’. Isso é útil para garantir que todas as imagens tenham o mesmo tamanho, o que é uma prática comum em modelos de aprendizado profundo para garantir a compatibilidade de entrada. Em seguida, é aplicada a transformação de “Rescaling”, que normaliza os valores dos pixels das imagens, dividindo cada valor de pixel pelo valor máximo possível (255 em imagens RGB). Isso comprime a escala de valores para o intervalo entre 0 e 1, o que é preferível para o treinamento de redes neurais, pois facilita a convergência e o aprendizado eficiente dos modelos.


<center>

![alt text](/assets/padroDados.png)

Imagem 3: Padronização dos dados (Autor, 2024)
</center>


## Executando o código

O código disponível no Colab, além de executar o que foi descrito nas seções anteriores com a classe de plantas tomate, também faz o mesmo processo com todas as classes de plantas mas com dados reduzidos. Esse fator é apenas para fins de novas possibilidades de uso dos dados, mas a definição do grupo até o momento é utilizar apenas o tomate. Para executar o código, acesse o Colab através do [LINK](https://colab.research.google.com/github/Wildemberg-Projects/Plants-Diseases/blob/main/main.ipynb) e execute cada uma das células em ordem.


