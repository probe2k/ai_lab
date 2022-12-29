import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

df = pd.read_csv("/home/probe/file.csv", names = names)

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2)
cf = KNeighborsClassifier(n_neighbors = 5).fit(xtrain, ytrain)
acc = cf.score(xtest, ytest)
print(acc)