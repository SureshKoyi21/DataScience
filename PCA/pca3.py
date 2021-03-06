import os
import pandas as pd
from sklearn import decomposition

#returns current working directory
os.getcwd()
#changes working directory
os.chdir("D:/Data Science/Data")

titanic_train = pd.read_csv("train.csv")

#EDA
titanic_train.shape
titanic_train.info()

titanic_train1 = pd.get_dummies(titanic_train, columns=['Pclass', 'Sex', 'Embarked'])
titanic_train1.shape
titanic_train1.info()

X_train = titanic_train1.drop(['PassengerId','Age','Cabin','Ticket', 'Name','Survived'], 1)
X_train.info()

#PCA games starts
pca = decomposition.PCA(n_components=4)
pca.fit(X_train)
print(pca.explained_variance_)
          
pca.explained_variance_ratio_.cumsum()

#Transformation of PCA happens here
transformed_X_train = pca.transform(X_train)
y_train = titanic_train['Survived']

