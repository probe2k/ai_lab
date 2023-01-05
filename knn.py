from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv('file.csv')

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2)
cf = KNeighborsClassifier(n_neighbors = 5).fit(xtrain, ytrain)
acc = cf.score(xtest, ytest)
print(acc)
