# -*- coding: utf-8 -*-
"""K-Means clustering

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l5zq0yxKf2WPZyKfSUhtmJ1mZxc57vAW
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


# %matplotlib inline

csv_file = "/content/Mall_Customers.csv"
data = pd.read_csv(csv_file)


print(data.head())


features = data[['Age', 'Annual Income (k$)']]

#Data Preprocess
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

#kMeans Model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_scaled)

#Prediction
y_kmeans = kmeans.predict(X_scaled)

#Visualisation
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y_kmeans, s=50, cmap='viridis')
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()