# Seleção dos modelos com potencial

# Remodelagem dos Dados

A fim de buscar melhor desempenho e por disponibilidade de RAM, os dados foram remodelados para metade dos pixels, agora com 128px. Além disso, os dados foram reduzidos em 50% da quantidade inicial, porém, foi utilizado data augmentation de forma a gerar variações das imagens em diferentes ângulos para que não ocorresse uma perda tão grande da qualidade do treinamento dada a redução dos dados. E para otimização do processo de treinamento do modelo, foi buscado variações dos lotes de imagens para reduzir o custo de hardware na execução do treinamento.


# Diversidade e Adequação dos Modelos Testados

No que diz respeito à diversidade e adequação dos modelos testados, o código apresenta uma abordagem abrangente. Ele começa carregando e pré-processando o conjunto de dados contendo as imagens de folhas de plantas com diferentes doenças. Essa etapa é crucial, pois fornece a base para o desenvolvimento e teste dos modelos de aprendizado de máquina.

A escolha de uma arquitetura de rede neural convolucional (CNN) no modelo é justificada devido à sua eficácia comprovada em problemas de classificação de imagens. A CNN é uma escolha adequada para este problema, pois permite a extração automática de características relevantes das imagens, como texturas e padrões, que são importantes para distinguir diferentes doenças nas folhas das plantas.

Além disso, o código incorpora técnicas de aumento de dados, como rotação e inversão, para aumentar a diversidade do conjunto de dados. Isso é importante para evitar overfitting e melhorar a capacidade do modelo de generalizar para novos dados. A Imagem 1 a seguir mostra o sumário e parâmetros do modelo 1 que foi testado e selecionado como o mais adequado.

<center>

![alt text](/assets/sumModelo1.png)

Imagem 1: Sumário do modelo 1 (Autor, 2024)
</center>

<br>

Devido às limitações da plataforma Google Colab e, também, de resultados provisórios do treinamento de outras versões do modelo, a versão 1 do modelo foi a melhor otimizada e com as melhores métricas como resultado dos testes. Portanto, neste documento contém apenas os resultados gerados pelo treinamento da versão 1.

Vale ressaltar que os outros modelos gerados estouraram o limite de uso da plataforma Google Colab durante seu treinamento, e geraram acurácia geral abaixo da média da versão, demonstrando assim que o modelo que melhor se adequa às especificações requisitadas.

## Análise Crítica do Desempenho

Quanto à análise crítica do desempenho, o código fornece uma análise detalhada dos resultados obtidos durante o treinamento dos modelos. Ele monitora várias métricas de desempenho, como acurácia, precisão, recall, sensibilidade, especificidade, F1-score, entre outros, ao longo do tempo de treinamento. Essas métricas são fundamentais para avaliar o quão bem o modelo está performando em diferentes aspectos, como a capacidade de identificar corretamente as doenças das folhas das plantas e evitar falsos positivos e falsos negativos.

Além disso, o código compara o desempenho de diferentes modelos, destacando suas vantagens e limitações. Isso é feito analisando não apenas as métricas de desempenho final, mas também o histórico de métricas ao longo do treinamento. Essa comparação permite uma avaliação mais completa do desempenho de cada modelo e ajuda na identificação dos modelos mais promissores para refinamento futuro.


<center>

![alt text](/assets/Metricas30Epocas.png)

Imagem 2:  Métricas de avaliação com 30 épocas do modelo 1 (Autor, 2024)


</center>

A Imagem 2 acima mostra o relatório final com todas as métricas de avaliação. Durante o treinamento do modelo 1, foi observado que a melhor acurácia final foi alcançada após 30 epochs. Isso indica que, após repetidas passagens pelos dados de treinamento e validação, o modelo atingiu seu melhor desempenho de classificação. Neste caso específico, 30 épocas foram suficientes para treinar o modelo e obter sua melhor acurácia e outras métricas. O tempo médio de treinamento foi de 1 hora  e 30 minutos.

## Executando o Código

Para executar o código, acesse o Colab através do [LINK](https://colab.research.google.com/github/Wildemberg-Projects/Plants-Diseases/blob/main/main.ipynb) e execute cada uma das células em ordem.