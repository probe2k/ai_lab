import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

df = pd.read_csv('play.csv')

# labelencoder domains might be different, check with df.head() before appending

le = LabelEncoder()
df['Outlook'] = le.fit_transform(df['Outlook'])
df['Temperature'] = le.fit_transform(df['Temperature'])
df['Humidity'] = le.fit_transform(df['Humidity'])
df['Wind'] = le.fit_transform(df['Wind'])
df['Play Tennis'] = le.fit_transform(df['Play Tennis'])

x = df.iloc[:, : -1]
y = df.iloc[:, -1]

classifier = tree.DecisionTreeClassifier(criterion = 'entropy').fit(x, y)
tree.plot_tree(classifier)
