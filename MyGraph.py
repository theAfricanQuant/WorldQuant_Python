# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt 
#from sklearn import linear_model
from scipy import stats
from sklearn.linear_model import LinearRegression

#import pylab 

#import numpy as np
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [193.09, 181.42, 175.1, 182.66, 169.47, 172.02, 169.86, 148.43]


x = np.array(x)
y = np.array(y)

x = np.reshape(x,-1)
y = np.reshape(y,-1)

gradient, intercept, r_value, p_value, std_err = stats.linregress(x,y)
mn=np.min(x)
mx=np.max(x)
x1=np.linspace(mn,mx,500)
y1=gradient*x1+intercept
plt.plot(x,y,'ob')
plt.plot(x1,y1,'-r')
plt.show()

model = LinearRegression()
model.fit(x, y)

X_predict = [9]  # put the dates of which you want to predict kwh here
y_predict = model.predict(X_predict)