#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:58:10 2018

@author: saumyaamehra
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:22:54 2018

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
                self.X.append(self.row[0:4])
                self.y.append(self.row[4])
            self.train()
        
    def train(self):
        import numpy as np
        
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler(feature_range = (0,1))
        self.X= np.array(self.X)
        self.y = np.array(self.y)
        self.scaled_X = scaler.fit_transform((self.X))
        print(self.scaled_X[0:4])
        self.scaled_y = scaler.fit_transform((self.y).reshape(-1,1))
        print(self.scaled_y[0:4])
        
        import keras 
        from keras import backend as K
        from keras.models import Sequential
        from keras.layers import Activation
        from keras.layers.core import Dense
        from keras.optimizers import Adam
        from keras.metrics import categorical_crossentropy
        
        model = Sequential()
        model.add(Dense(2000, input_dim=(4),activation = 'tanh'))
        model.add(Dense(1000, activation = 'tanh'))
        
        model.add(Dense(1000, activation = 'tanh'))
        model.add(Dense(1000, activation = 'sigmoid'))
        model.add(Dense(500, activation = 'sigmoid'))
 #       model.add(Dense(1000, activation = 'tanh'))
        model.add(Dense(500, activation = 'tanh'))
        model.add(Dense(200, activation = 'tanh'))
##        #model.add(Dense(50, activation = 'relu'))
        model.compile(Adam(lr=0.01),loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
#        
#       print("Model saved")
        print(model.summary())
        
        model.fit(self.scaled_X, self.scaled_y, batch_size = 10, epochs= 30,shuffle = True, verbose=2)
        
           
       
           
            
        
        
        
        
        
   
obj = file("/Users/saumyaamehra/Desktop/all_data1.csv") 
