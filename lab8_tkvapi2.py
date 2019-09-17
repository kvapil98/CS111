# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:32:45 2017

@author: kvapil98
"""

import csv
import matplotlib.pyplot as plt
import random

def plot_data(file_name, x, y):
    '''This func plots three different flowers and the x and y axis for each flower'''
    setosa_x=[]
    setosa_y=[]
    versicolor_x=[]
    versicolor_y=[]
    virginica_x=[]
    virginica_y=[]
    
    with open(file_name, 'r') as flower_graph:
        file = csv.reader(flower_graph)
        for row in file: #loop that adds given x and y to three different species
            
            if len(row)==0:
                continue
            
            if row[4] == 'Iris-setosa':
                setosa_x.append(float(row[x]))
                setosa_y.append(float(row[y]))
            
            if row[4] == 'Iris-versicolor':
                versicolor_x.append(float(row[x]))
                versicolor_y.append(float(row[y]))
            
            if row[4] == 'Iris-virginica':
                virginica_x.append(float(row[x]))
                virginica_y.append(float(row[y]))
    
    plt.plot(setosa_x, setosa_y, 'b.')
    plt.plot(versicolor_x, versicolor_y, 'y.')
    plt.plot(virginica_x, virginica_y, 'r.')
    plt.show()

def plot_random(file_name,x,y,n):
    '''This func plots the random values of all the flower species with the given x and y'''
    total_x = [] #all values for x
    total_y = [] #all values for y
    random_x = [] #all random values for x
    random_y = [] #all random values for y
    
    with open(file_name,'r') as flower_graph:
        file = csv.reader(flower_graph)
        for row in file: #loop puts all of x and y in given list
            if len(row) == 0:
                continue
            
            total_x.append(float(row[x]))
            total_y.append(float(row[y]))
    
            #print(total_x)
            #print(total_y)
    high_x = max(total_x)
    #print(high_x)
    low_x = min(total_x)
    #print(low_x)
    high_y = max(total_y)
    #print(high_y)
    low_y = min(total_y)
    #print(low_y)
    
    for i in range(n): #loop iterates for amount the user wants
        x = random.uniform(low_x, high_x)
        random_x.append(x)
        y = random.uniform(low_y, high_y)
        random_y.append(y)
    #print(random_x)
    #print(random_y)
    
    plt.plot(random_x,random_y,'b.')
    plt.show()

#When comparing the two graphs, the graphs are very different.The random graph produces a very random scatter plot
#While the data plot shows linear patterns for each type of species but the random does not
#This is because the random plot is all random and it takes from all the species 