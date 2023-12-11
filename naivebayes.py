import pandas as pd
import numpy as np

data = pd.read_csv("iris.csv")
x = data.iloc[:,:4].values
y = data.iloc[:,4].values
print(x)
print(y)
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=3)

from sklearn.naive_bayes import GaussianNB
gb = GaussianNB()
gb.fit(x_train,y_train)
prediction = gb.predict(x_test)
print("Predicted",prediction)
print("Actual",y_test)

# score = gb.score(x_test,y_test)
# print(score)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,prediction)
print(cm)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test,prediction)*100
print(acc)