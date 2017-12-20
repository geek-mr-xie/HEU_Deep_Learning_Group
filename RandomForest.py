#coding = utf8

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import cross_validation

# trainFile
# testFile
trainData = pd.read_csv("train.csv")
testData = pd.read_csv("test.csv")

label = trainData['label']
X = trainData.drop('label', 1)

clf = RandomForestClassifier(n_estimators=200, n_jobs=-1, max_depth=50)

scores = cross_validation.cross_val_score(clf, X, label, cv=5)
print(scores)
'''
clf.fit(X, label)
preds = clf.predict(testData)
'''
