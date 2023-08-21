# k-vizinho mais próximo

## Sobre o algoritmo:
O algoritmo "k-vizinho mais próximo" (k-nearest neighbors, ou k-NN em inglês) é um método de classificação e regressão em aprendizado de máquina. Ele é usado para classificar um novo ponto de dados com base na maioria dos k pontos de dados vizinhos mais próximos no espaço de características.

### O funcionamento básico do algoritmo k-NN:

- Dados de Treinamento: Você precisa de um conjunto de dados de treinamento com pontos já classificados ou rotulados.

- Distância: O algoritmo usa uma medida de distância (por exemplo, distância euclidiana) para calcular a proximidade entre os pontos de dados.

- Escolha de k: Você seleciona um valor para k, que é o número de vizinhos mais próximos a serem considerados.

- Classificação ou Regressão: Para classificação, os rótulos dos k vizinhos mais próximos são contados e o rótulo mais frequente é atribuído ao novo ponto. Para regressão, os valores dos k vizinhos mais próximos são usados para calcular uma média ou um valor ponderado para prever o valor do novo ponto.

- Atribuição ou Previsão: O ponto de dados em questão é classificado ou previsto com base nas decisões tomadas nos passos anteriores.

É importante observar que o valor de k é um hiperparâmetro crítico. Um valor muito pequeno pode levar a uma classificação ruidosa e sensível a outliers, enquanto um valor muito grande pode resultar em uma generalização insuficiente.