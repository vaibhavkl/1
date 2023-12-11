import pandas as pd
import numpy as np
data=pd.read_csv("iris.csv")
x = data.iloc[:,:4].values
y = data.iloc[:,4].values

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size = 0.30) 

from sklearn.ensemble import RandomForestClassifier 

data = pd.DataFrame({'sepallength': x[:, 0], 'sepalwidth': x[:, 1], 
					'petallength': x[:, 2], 'petalwidth': x[:, 3], 
					'species': y}) 

clf = RandomForestClassifier(n_estimators = 100) 
clf.fit(X_train, y_train) 
y_pred = clf.predict(X_test) 
from sklearn.metrics import accuracy_score
print("ACCURACY OF THE MODEL: ", accuracy_score(y_test, y_pred)) 

# predicting which type of flower it is. 
print(clf.predict([[3, 3, 2, 2]])) 