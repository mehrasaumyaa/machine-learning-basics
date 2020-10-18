#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:22:30 2018

@author: saumyaamehra
"""

        
class file:
    
    def __init__(self,filename):
        import csv
        with open(filename,'r') as csvFile:
            filereader = csv.reader(csvFile, delimiter=',')
            
            self.theList=[]
            self.X=[]
            self.y=[]
            for self.row in filereader:
                self.X.append(self.row[0:10])
                self.y.append(self.row[10])
            self.train()
        
    def train(self):
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors=1)

#        knn.fit(self.X,self.y)
#        print(knn.predict([[0,0,1,0,0,0,0,0,0,0]]))
#        print(knn.predict([[0,0,0,0,0,0,0,0,0,0]]))
#        print(knn.predict([[3,5,8,9,6,10,5,7,4,9]]))
        import numpy as np
        from sklearn.cross_validation import train_test_split
        Xtrain, Xtest, ytrain, ytest = train_test_split(self.X,self.y,test_size=0.4, random_state=4) 
        X_train = np.array(Xtrain)
        X_test = np.array(Xtest)
        y_train = np.array(ytrain)
        y_test = np.array(ytest)
     
        knn.fit(X_train,y_train)
        y_pred = knn.predict(X_test)
        
        from sklearn import metrics
        print(metrics.accuracy_score(y_test,y_pred))
           
       
           
            
   
obj = file("/Users/saumyaamehra/Desktop/all_data1.csv") 


    
    
    