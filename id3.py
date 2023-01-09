import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from collections import Counter

def id3(df, target, attribute, default_class = None):
	counter = Counter(x for x in df[target])
	if len(counter) == 1:
		return next(iter(counter))
	elif df.empty or (not attribute):
		return default_class
	else:
		gain = mutual_info_classif(df[attribute], df[target], discrete_features = True)
		index = gain.tolist().index(max(gain))
		best_attr = attribute[index]
		tree = {best_attr: {}}
		rem_attr = [i for i in attribute if i != best_attr]

		for attr, data in df.groupby(best_attr):
			tree[best_attr][attr] = id3(data, target, rem_attr, default_class)
		return tree

df = pd.read_csv('file.csv')
attribute = df.columns.tolist()
attribute.remove('answer')
for cols in df.select_dtypes("object"):
	df[cols], _ = df[cols].factorize()
print(id3(df, 'answer', attribute))
