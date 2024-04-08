# Definição do problema e contextualização

## Objetivo
O objetivo deste mini trabalho é estabelecer as bases para o projeto de Aprendizado de Máquina (ML) que visa desenvolver um software capaz de analisar imagens de plantas com doenças e identificar o tipo de doença presente. Para isso, é essencial definir claramente o problema a ser abordado, compreender o contexto no qual ele está inserido e estabelecer objetivos específicos para a solução proposta. Além disso, é importante realizar uma análise do cenário atual, identificando soluções existentes, lacunas e possíveis melhorias. Por fim, devem ser escolhidas e justificadas as métricas de avaliação de desempenho alinhadas com os objetivos do projeto, estabelecendo um patamar mínimo de desempenho esperado para considerar o projeto bem-sucedido.


## Cenário Atual e contexto

A agricultura desempenha um papel fundamental na sustentabilidade alimentar global, fornecendo alimentos essenciais para a população mundial. No entanto, a saúde das plantas, fundamental para a produção agrícola, está constantemente ameaçada por uma variedade de fatores, incluindo doenças. Estas podem ser causadas por fungos, vírus, bactérias, deficiências nutricionais, entre outros agentes patogênicos. Atualmente, a detecção e diagnóstico de doenças em plantas são predominantemente realizados manualmente por agrônomos e especialistas em agricultura. Este processo é muitas vezes demorado, intensivo em mão de obra e sujeito a erros humanos. Além disso, a capacidade dos especialistas em identificar doenças pode variar, o que pode resultar em diagnósticos imprecisos e tratamentos inadequados. Embora soluções computacionais baseadas em técnicas de processamento de imagens e aprendizado de máquina tenham sido desenvolvidas para auxiliar na detecção de doenças em plantas, muitas delas enfrentam desafios significativos. Essas soluções podem ser limitadas em termos de precisão, velocidade de processamento e capacidade de generalização para diferentes tipos de plantas e doenças. Isso pode resultar em diagnósticos imprecisos ou ineficazes, prejudicando a eficácia das medidas de controle e prevenção. A introdução de um software de Aprendizado de Máquina capaz de analisar imagens de plantas e identificar com precisão o tipo de doença presente teria um impacto significativo no cenário atual da agricultura. Uma solução eficaz e precisa permitiria uma detecção mais rápida e confiável de doenças em plantações possibilitando a implementação de medidas preventivas e curativas de forma mais ágil e eficiente. Isso poderia resultar em redução de perdas na produção agrícola, aumento da eficiência dos sistemas de cultivo e, consequentemente, contribuir para a segurança alimentar global.

## Métricas de avaliação e desempenho

- Acurácia: 

  Justificativa: A acurácia é uma métrica fundamental para avaliar a precisão geral do modelo na classificação das doenças das plantas. Uma alta acurácia indica que o modelo está fazendo previsões corretas na maioria dos casos, o que é crucial para garantir diagnósticos precisos e confiáveis. 
  
  Patamar Mínimo de Desempenho: O patamar mínimo de acurácia esperado para considerar o projeto bem-sucedido será de 85%. Isso significa que o modelo deve ser capaz de classificar corretamente pelo menos 85% das imagens de plantascom doenças.
  
- Precisão: 

  Justificativa: A precisão é importante para avaliar a proporção de verdadeiros positivos em relação ao total de predições positivas. Uma alta precisão é essencial para garantir que o modelo minimize os falsos positivos, evitando diagnósticos incorretos que possam levar a tratamentos desnecessários ou inadequados. 
  
  Patamar Mínimo de Desempenho: O patamar mínimo de precisão esperado será de 80%. Isso significa que o modelo deve ser capaz de identificar corretamente pelo menos 80% das plantas diagnosticadas como portadoras de doenças. - Revocação: Justificativa: A revocação é importante para avaliar a proporção de verdadeiros positivos em relação ao total de casos positivos reais. Uma alta revocação é crucial para garantir que o modelo minimize os falsos negativos, ou seja, que não deixe de identificar plantas doentes. Patamar Mínimo de Desempenho: O patamar mínimo de revocação esperado será de 80%. Isso significa que o modelo deve ser capaz de identificar corretamente pelo menos 80% das plantas que realmente estão doentes. 

  - F1-Score: 

  Justificativa: O F1-Score é uma medida que combina precisão e revocação, fornecendo uma avaliação geral do equilíbrio entre essas duas métricas. Um alto F1-Score indica um bom equilíbrio entre a capacidade do modelo de identificar corretamente casos positivos e negativos. 
  
  Patamar Mínimo de Desempenho: O patamar mínimo de F1-Score esperado será de 0.8. Isso significa que o modelo deve alcançar um F1-Score de pelo menos 0.8 para considerar o projeto bem-sucedido.