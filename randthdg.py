# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:25:03 2018

@author: WelCome
"""
import random
import csv
 

def check_no_cycles(A):
	reached = [False for i in range(len(A))]
	return dfs_cycles(A, 0, -1, reached) 
 
def dfs_cycles(A, start, parent, reached):
	reached[start] = True
	for i in range(len(A)):
		if A[start][i] != 0:
			if not reached[i]:
				if not dfs_cycles(A, i, start, reached): 
					return False
			elif i != parent:
				return False  
	return True

def check_connectedness(A):
	reached = [False for i in range(len(A))]
	reach_dfs(A, 0, reached) 
	return False not in reached
 
def reach_dfs(A, start, reached):
	reached[start] = True
	for i in range(len(A)):
		if A[start][i] != 0 and not reached[i]:
			reach_dfs(A, i, reached)
	return
def random_adjacency_matrix(n,f):
    d_c = 0
    A = [[random.randint(0, 1) for i in range(n)] for j in range(n)]
    
    for i in range(n):
        A[i][i] = 0
        
    for i in range(n):
        for j in range(n):
            A[j][i]=A[i][j]
    
            
    for j in range(0,100):        
     for i in range (0, n):
        print (A[i])
    
        
     if check_connectedness(A) == True and check_no_cycles(A)==True:
            d_c=d_c+1
           
            for i in range(n):
                for j in range(n):
                    t=str(A[i][j])
                    f.write(t)
                    f.write(',')
            f. write('0')
            f.write("\n")           
            
          
            print('graph is a tree')
     else:
         
           
             for i in range(n):
                for j in range(n):
                    t=str(A[i][j])
                    f.write(t)
                    f.write(',')
             f. write('1')
             f.write("\n")
             
             print('graph is not a tree')
     print('\n')
     return d_c


       
           
            
    
outer_c=0

with open('pr.csv', 'w') as f:    
 for x in range (0,200000):
   outer_c= outer_c + random_adjacency_matrix(8,f)
print(outer_c)