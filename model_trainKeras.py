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
                self.X.append(self.row[0:10])
                self.y.append(self.row[10])
            self.train()
        
    def train(self):
        import numpy as np
        
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler(feature_range = (0,1))
        self.X= np.array(self.X)
        self.y = np.array(self.y)
        self.scaled_X = scaler.fit_transform((self.X))
        self.scaled_y = scaler.fit_transform((self.y).reshape(-1,1))
        
        import keras 
        from keras import backend as K
        from keras.models import Sequential
        from keras.layers import Activation
        from keras.layers.core import Dense
        from keras.optimizers import Adam
        from keras.metrics import categorical_crossentropy
        
        model = Sequential()
        model.add(Dense(50000, input_dim=(10),activation = 'tanh'))
        model.add(Dense(10000, activation = 'tanh'))
        
        #from keras.utils.vis_utils import plot_model
        #plot_model(model,to_file='model_plot.png',show_shapes=True,show_layer_names=True)
        #model.add(Dense(7000, activation = 'tanh'))
#        model.add(Dense(1000, activation = 'tanh'))
        model.add(Dense(100, activation = 'tanh'))
        model.add(Dense(100, activation = 'sigmoid'))
        model.add(Dense(100, activation = 'tanh'))
        model.add(Dense(100, activation = 'tanh'))
 #       model.add(Dense(500, activation = 'tanh'))
##        #model.add(Dense(50, activation = 'relu'))
        model.compile(Adam(lr=0.01),loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
#        
#        from keras.utils import plot_model
#        plot_model(model, to_file='model.png')
#        print("Model saved")
 #       print(model.summary())
        
        model.fit(self.scaled_X, self.scaled_y, batch_size = 1000, epochs= 30,shuffle = True, verbose=2)
        
           
       
           
            
        
        
        
        
        
   
obj = file("/Users/saumyaamehra/Desktop/all_data1.csv") 
