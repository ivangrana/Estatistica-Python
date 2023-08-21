import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Generate example data with two classes
np.random.seed(42)
class_0 = np.random.randn(50, 2) + [2, 2]
class_1 = np.random.randn(50, 2) + [6, 6]
X = np.vstack((class_0, class_1))
y = np.array([0] * 50 + [1] * 50)

# KNN classification
def knn_predict(X_train, y_train, x, k=3):
    distances = [np.sqrt(np.sum((x - x_train)**2)) for x_train in X_train]
    k_indices = np.argsort(distances)[:k]
    k_nearest_labels = [y_train[i] for i in k_indices]
    most_common = Counter(k_nearest_labels).most_common(1)
    return most_common[0][0]

# Generate a mesh grid for visualization
h = 0.1
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Make predictions on the mesh grid
mesh_predictions = np.array([knn_predict(X, y, np.array([xx[i, j], yy[i, j]])) for i in range(xx.shape[0]) for j in range(xx.shape[1])])
mesh_predictions = mesh_predictions.reshape(xx.shape)

# Plot the data points and decision boundary
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, mesh_predictions, alpha=0.3, cmap='coolwarm')
plt.scatter(class_0[:, 0], class_0[:, 1], marker='o', label='Class 0', edgecolors='k')
plt.scatter(class_1[:, 0], class_1[:, 1], marker='x', label='Class 1', edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Nearest Neighbors Decision Boundary')
plt.legend()
plt.show()
