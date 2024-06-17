# Análise exploratória dos dados

Durante esta fase, realizou-se uma análise das imagens de plantas presentes
no conjunto de dados selecionado, associando cada imagem à sua respectiva
categoria indicada pela label (etiqueta).

As labels, em inglês, que distinguem os diversos tipos de plantas saudáveis e
doentes estão organizadas da seguinte maneira:
<center>
<b>Número de identificação - Espécie de planta - Tipo de Doença</b>
</center>
Por exemplo: 3. Apple___healthy, onde o número de identificação é 3, a
espécie de planta é maçã e o tipo de doença é saudável.


|Nº|Espécie|Tipo de Doença|Label|
|-|-|-|-|
|0|Apple |Apple_scab|0. Apple___Apple_scab|
|1|Apple |Black_rot|1. Apple___Black_rot|
|2|Apple |Cedar_apple_rust|2. Apple___Cedar_apple_rust|
|3|Apple |healthy|3. Apple___healthy|
|4|Blueberry|healthy|4. Blueberry___healthy|
|5|Cherry|healthy|5. Cherry___healthy|
|6|Cherry|Powdery_mildew|6. Cherry___Powdery_mildew|
|7|Corn|Cercospora_leaf_spotGray_leaf_spot|7. Corn___Cercospora_leaf_spotGray_leaf_spot|
|8|Corn|Common_rust|8. Corn___Common_rust|
|9|Corn|healthy|9. Corn___health|
|10|Corn|Northern_Leaf_Blight|10. Corn___Northern_Leaf_Blight|
|11|Grape|Black_rot|11. Grape___Black_ro|
|12|Grape|Esca(Black_Measles)| 12. Grape___Esca(Black_Measles)|
|13|Grape|healthy|13. Grape___healthy|
|14|Grape|Leaf_blight(Isariopsis_Leaf_Spot)|14.Grape___Leaf_blight(Isariopsis_Leaf_Spot)|
|15|Orange|Haunglongbing(Citrus_greening)|15.Orange___Haunglongbing(Citrus_greening)|
|16|Peach|Bacterial_spot|16. Peach___Bacterial_spot|
|17|Peach|healthy|17. Peach___healthy|
|18|Pepper,bell|Bacterial_spot|18. Pepper,bell___Bacterial_spot|
|19|Pepper,bell|healthy|19. Pepper,bell___healthy|
|20|Potato|Early_blight|20. Potato___Early_blight|
|21|Potato|healthy|21. Potato___healthy|
|22|Potato|Late_blight|22. Potato___Late_blight|
|23|Raspberry|healthy|23. Raspberry___healthy|
|24|Soybean|healthy|24. Soybean___healthy|
|25|Squash|Powdery_mildew|25. Squash___Powdery_mildew|
|26|Strawberry|healthy|26. Strawberry___healthy|
|27|Strawberry|Leaf_scorch|27. Strawberry___Leaf_scorch|
|28|Tomato|Bacterial_spot|28. Tomato___Bacterial_spot|
|29|Tomato|Early_blight|29. Tomato___Early_blight|
|30|Tomato|healthy|30. Tomato___healthy|
|31|Tomato|Late_blight|31. Tomato___Late_blight|
|32|Tomato|Leaf_Mold|32. Tomato___Leaf_Mold|
|33|Tomato|Septoria_leaf_spot|33. Tomato___Septoria_leaf_spot|
|34|Tomato|Spider_mites Two-spotted_spider_mite|34. Tomato___Spider_mitesTwo-spotted_spider_mite|
|35|Tomato|Target_Spot|35. Tomato___Target_Spot|
|36|Tomato|Tomato_mosaic_virus|36. Tomato___Tomato_mosaic_virus|
|37|Tomato|Tomato_Yellow_Leaf_Curl_Virus|37.Tomato___Tomato_Yellow_Leaf_Curl_Virus|

## Dados retornados do dataframe

A estrutura total do dado retornado no data frame criado inclui as seguintes
colunas:

- image: Esta coluna contém os dados das imagens representadas por matrizes tridimensionais.
- filename: Esta coluna contém os nomes dos arquivos das imagens, fornecendo informações sobre a origem de cada imagem no conjunto de dados.
- label: Esta coluna contém os números das etiquetas associadas a cada imagem.

![alt text](/assets/dadosRetDataframe.jpg)

<br>

O exemplo abaixo descreve uma imagem representada por uma matriz tridimensional, onde cada valor dentro da matriz representa a intensidade de cor de um pixel. A estrutura da matriz é (244, 244, 3), onde:

- O primeiro número, 244, representa a altura da imagem, ou seja, quantos pixels a imagem tem na vertical.

- O segundo número, também 244, indica a largura da imagem, ou seja, quantos pixels a imagem tem na horizontal.

- O terceiro número, 3, denota a quantidade de canais de cores da imagem, indicando que a imagem está no formato RGB (Red, Green, Blue), com cada pixel representado por uma combinação de três valores numéricos que correspondem à intensidade de vermelho (R), verde (G) e azul (B)

<center>
![alt text](/assets/imgMatrizTri.png)
</center>

A matriz mostrada é um recorte da imagem, com valores numéricos representando as intensidades de cor de cada pixel. Por exemplo, o primeiro pixel tem intensidades de [171, 161, 169] para os canais vermelho, verde e azul, respectivamente. Cada conjunto de valores [R, G, B] representa a cor do pixel na posição correspondente da imagem.

Além disso, a label associada a essa imagem é 35, servindo para categorizá-la em um dos tipos de doenças ou estado de saúde da planta, conforme o sistema de categorização estabelecido anteriormente. O exemplo a seguir é uma imagem categorizada na label 35 (Tomato___Target_Spot):

<center>

![alt text](/assets/tomatoleaf.png)

</center>

## Executando código

Acesse o código no Colab através do [LINK](https://colab.research.google.com/github/Wildemberg-Projects/Plants-Diseases/blob/main/main.ipynb) e execute cada uma das células em ordem. O código demonstra o que foi apresentado na subseção anterior, além de gerar um gráfico relacionando a quantidade de labels com a quantidade de imagens de cada uma das labels.

## Identificação de padrões e correlações

Foi feito também um script no Colab [LINK](https://colab.research.google.com/drive/1E3BpsvRtIG9av8VeCKSVSbj8QCpayWf3?usp=sharing) com a finalidade de obter estatísticas a partir de uma pequena amostra de dados. Esse script demonstra um gráfico de quantas imagens tem para cada tipo de doença, além de mostrar exemplos de imagens para checar suas qualidades. 

O algoritmo de identificação de padrões aplicado ao dataset Plant_Village coletará características visuais das imagens das plantas, incluindo padrões de textura, forma, cor e estruturas específicas associadas a doenças ou condições saudáveis. Essas características serão extraídas através de camadas convolucionais em uma rede neural convolucional (CNN). Durante o treinamento, o algoritmo aprenderá a associar essas características às labels correspondentes, como diferentes doenças de plantas ou condições saudáveis. Assim, quando uma nova imagem de planta for fornecida como entrada, o algoritmo aplicará suascaracterísticas aprendidas para realizar a classificação, determinando a doença ou condição da planta com base nas semelhanças com os exemplos de treinamento previamente rotulados.