# Otimização e ajuste fino do sistema

## Otimização de Hiperparâmetros

É clara a importância de realizar testes utilizando o conceito da mudança de hiperparâmetros, uma vez que estes artefatos alteram de forma direta a estrutura do modelo podendo gerar diferentes resultados de métricas ao final dos testes.

Durante o desenvolvimento do Mini Trabalho 5, o grupo realizou testes de otimização, na versão 1 do modelo, se aproveitando da mudança de hiperparâmetros. Focou-se, principalmente, na mudança do número de “Epochs” e após os resultados coletados, que serão exibidos nas imagens 1, 2, 3 e 4, concluiu-se que o número ideal de epochs é de 30 em um primeiro momento.

<center>

![alt text](/assets/Treino25.png)

Imagem 1: Resultado do treinamento utilizando 25 epochs (Autor, 2024)

![alt text](/assets/Treino32.png)

Imagem 2: Resultado do treinamento utilizando 32 epochs (Autor, 2024)

![alt text](/assets/Treino35.png)

Imagem 3: Resultado do treinamento utilizando 35 epochs (Autor, 2024)

![alt text](/assets/Treino30.png)

Imagem 4: Resultado do treinamento utilizando 30 epochs (Autor, 2024)

</center>


## Validação Cruzada

O uso de técnicas de validação cruzada é essencial para avaliar o desempenho dos modelos de forma mais robusta e evitar o sobreajuste. No código fornecido, a validação cruzada é implementada utilizando uma abordagem de divisão dos dados em conjuntos de treinamento, validação e teste.

Além disso, o código utiliza um método similar ao “KFold” para dividir os dados em grupos e realizar o treinamento do modelo de forma iterativa, garantindo uma avaliação abrangente do desempenho do modelo em diferentes conjuntos de dados.

## Melhoria no desempenho

Para demonstrar a eficácia da otimização de hiperparâmetros, foram realizados experimentos de treinamento do modelo com diferentes configurações de hiperparâmetros. O principal hiperparâmetro alterado foi o número de épocas que o modelo processaria. O desempenho do modelo foi avaliado por meio de métricas de avaliação como acurácia, precisão, recall, F1-score, sensibilidade, especificidade, entre outras.

Em adição, no desenvolvimento deste Mini Trabalho, foi realizado a implementação do um novo modelo, desta vez, utilizando Deep Learning, e foi posto o modelo para treinamento utilizando 30 epochs, onde obtivemos as seguintes métricas finais (Imagem 6), mostrando assim a evolução do modelo em relação à versão 1 do Mini Trabalho 5 (Imagem 5).

<center>

![alt text](/assets/MetriV1.png)

Imagem 5:   Métricas obtidas no modelo V1 (Autor, 2024)

![alt text](/assets/MetriV2.png)

Imagem 6:   Métricas obtidas no modelo V2 (Autor, 2024)

</center>

Além disso, no código fornecido, foi realizada otimização utilizando o otimizador Adam com uma taxa de aprendizado de 0.001, beta_1 de 0.9, beta_2 de 0.999, epsilon de 0.1 e decaimento de 0.0, a fim de melhorar o desempenho do modelo. Junto a isso, são adotadas diversas técnicas, como aumento de dados, normalização, regularização, entre outras. Após a implementação dessas técnicas, otimizações e ajustes dos hiperparâmetros, o tempo médio de treinamento passou de 1h30min (tempo médio apresentado no Mini Trabalho 5) para 30min (Imagem 7), tempo três vezes menor.


<center>

![alt text](/assets/TempoObtidoTreino.png)

Imagem 7:  Métricas de avaliação com 30 épocas do modelo 1 (Autor, 2024)

</center>

## Executando Código

Para executar o código, acesse o Colab através do [LINK](https://colab.research.google.com/github/Wildemberg-Projects/Plants-Diseases/blob/main/main.ipynb) e execute cada uma das células em ordem.