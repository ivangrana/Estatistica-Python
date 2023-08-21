import numpy as np
from collections import Counter

class ClassificadorKNN:
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X, y):
        """recebe os dados de treinamento X (características) e y (rótulos)"""
        self.X_train = X
        self.y_train = y
        
    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)
    
    def _predict(self, x):
        """calcula a previsão para um único ponto X"""
        #Calcula as distâncias entre o ponto x e todos os pontos de treinamento usando a fórmula da distância euclidiana.
        distancia_euclidiana = [np.sqrt(np.sum((x - x_train)**2)) for x_train in self.X_train] 
        k_indices = np.argsort(distancia_euclidiana)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices] #rotula
        rotulos_mais_comuns = Counter(k_nearest_labels).rotulos_mais_comuns(1)
        return rotulos_mais_comuns[0][0]

# Generate example data
X = np.random.rand(100, 2)
y = np.random.randint(0, 2, 100)

# Split the data into training and testing sets
X_train, X_test = X[:80], X[80:]
y_train, y_test = y[:80], y[80:]

# Create and fit the KNN classifier
knn_classifier = ClassificadorKNN(k=3)
knn_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = knn_classifier.predict(X_test)

# Calculate accuracy
accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy:.2f}")
