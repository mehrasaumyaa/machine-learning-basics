#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:01:53 2018

@author: saumyaamehra
"""

import pandas as pd
data = pd.read_csv("http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv",index_col=0)

 
import seaborn as sns

#sns.pairplot(data,x_vars= ['TV','radio','newspaper'], y_vars = 'sales',size=5, aspect = 0.7, kind = "reg")
feature_cols = ['TV', 'radio', 'newspaper']
X=data[feature_cols]
#print(X.head())
y= data['sales']
#print(y.head())

from sklearn.cross_validation import train_test_split
X_train,X_test, y_train, y_test = train_test_split(X,y,random_state=1)

from sklearn.linear_model import LinearRegression
linreg= LinearRegression()
linreg.fit(X_train,y_train)
print(linreg.intercept_)
print(linreg.coef_)
print(zip(feature_cols, linreg.coef_))

true = [100,50,30,20]
pred = [90,50,50,30]

from sklearn import metrics
import numpy as np
print(metrics.mean_squared_error(true,pred))