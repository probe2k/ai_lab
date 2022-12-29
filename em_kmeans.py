from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
df = pd.read_csv('file.csv', names = names)

plt.subplot(2, 2, 1)
plt.title('Real')
plt.scatter(df.Petal_Length, df.Petal_Width, c = 'red')

model = KMeans(n_clusteres = 3, random_state = 0).fit(df.iloc[:, :-1])
plt.subplot(2, 2, 2)
plt.title('KMeans')
plt.scatter(df.Petal_Length, df.Petal_Width, c = 'blue')

gmm = GaussianMixture(n_components = 3, random_state = 0).fit(df.iloc[:, :-1])
plt.subplot(2, 2, 3)
plt.title('GMM')
plt.scatter(df.Petal_Length, df.Petal_Width, c = 'green')

plt.show()