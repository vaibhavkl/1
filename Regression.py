#Assignment based on simple linear regression on any dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  sklearn.linear_model import LinearRegression
data=pd.read_csv("housing.csv")
#print(data.columns)
f=['price', 'area']
data=data[f]
print(data)
x=data.iloc[:,1:].values
print("independent variable area as x \n",x)
y=data.iloc[:,:1].values
print("Dependent variable price as y \n", y)
#split data into training and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=3)
#print(x_train)
reg=LinearRegression()
reg.fit(x_train,y_train)
prediction=reg.predict(x_test)
print(prediction)
print(y_test)



#calculating mse,rmse and r-squre
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,prediction)
print("mean squeare error: \n",mse)

r2score=reg.score(x_test,y_test)
print(r2score)
print("weight or slope M is : \n",reg.coef_)
print("intercept C is :\n",reg.intercept_)
plt.scatter(x_test,y_test)
plt.plot(x_test, prediction, color = "g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()





'''
1. Find a linear regression equation for the following two sets of data:




x       2 4 6 8

y       3 7 5 10




Sol: To find the linear regression equation we need to find the value of Σx 20, Σy 25, Σx2=120



and Σxy 144 

Construct the table and find the value

























The formula of the linear equation is y=a+bx. Using the formula we will find the value of a and b

a= (∑Y)(∑X2)−(∑X)(∑XY)
n(∑x2)−(∑x)2

Now put the values in the equation

a=25×120−20×144
    4×120−400


a= 120
    80

a=1.5


b= n(∑XY)−(∑X)(∑Y)
n(∑x2)−(∑x)2
Put the values in the equation


b=4×144−20×25
    4×120−400


b=7680

b=0.95

Hence we got the value of a = 1.5 and b = 0.95

The linear equation is given by

Y = a + bx

Now put the value of a and b in the equation

Hence equation of linear regression is y = 1.5 + 0.95x

'''