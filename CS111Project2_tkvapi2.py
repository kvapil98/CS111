# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:09:58 2017

@author: kvapil98
"""

import matplotlib.pyplot as plt
import random

def make_founders(red, purple, blue):
    '''randomizes list of founders'''
    population = []
    for i in range(red):
        population.append('r')
    for i in range(purple):
        population.append('p')
    for i in range(blue):
        population.append('b')
    random.shuffle(population)
    return population

def mate_pair_once(allele1,allele2):
    '''creates all possible outcomes of pairs'''
    if allele1 == 'r' and allele2 == 'r':
        return 'r'
    if allele1 == 'b' and allele2 == 'b':
        return 'b'
    if allele1 == 'p' and allele2 == 'p':
        new = random.choice('bpr')
        return new
    if allele1 == 'p' and allele2 == 'r':
        new = random.choice('rp')
        return new
    if allele1 == 'p' and allele2 == 'b':
        new = random.choice('rb')
        return new
    if allele1 == 'r' and allele2 == 'p':
        new = random.choice('rp')
        return new
    if allele1 == 'b' and allele2 == 'p':
        new = random.choice('pb')
        return new
    if allele1 == 'r' and allele2 == 'b':
        return 'p'
    if allele1 == 'b' and allele2 == 'r':
        return 'p'
        

def mate_pair(al1,al2,n):
    '''mates pairs for a set amount of times'''
    total_pair = []
    for i in range(n):
        total_pair.append(mate_pair_once(al1,al2))
    return total_pair

def create_generation(lis,num):
    '''creates a generation of a set amount of matings'''
    random.shuffle(lis)
    #print(lis)
    gen_ls = []
    i = 0
    ii = 1
    if len(lis) % 2 != 0:
        lis.pop()
    while ii <= len(lis):
        new_ph = mate_pair(lis[i],lis[ii],num)
        #print(new_ph)
        gen_ls.extend(new_ph)
        i += 2
        ii += 2
    return gen_ls

def calc_freq(lis):
    '''calculates frequencies of each phenotype'''
    freq_list = []
    
    r = lis.count('r')
    p = lis.count('p')
    b = lis.count('b')
    
    if r == 0:
        freq_list.append(0)
    else:
        freq_list.append(r/len(lis))
    if p == 0:
        freq_list.append(0)
    else:
        freq_list.append(p/len(lis))
    if b == 0:
        freq_list.append(0)
    else:
        freq_list.append(b/len(lis))
    
    return freq_list

def pop_sim(red, purple, blue, offspring, gen):
    '''creates a population simulator over a set amount of generations'''
    founders = make_founders(red, purple, blue)
    g = list(range(gen))
    red = []
    purple = []
    blue = []
    for i in range(gen):
        show_list = []
        new_gen = create_generation(founders,offspring)
        freq_list = calc_freq(new_gen)
        
        red.append(freq_list[0])
        show_list.append(freq_list[0])
        purple.append(freq_list[1])
        show_list.append(freq_list[1])
        blue.append(freq_list[2])
        show_list.append(freq_list[2])
        
        print(show_list)
        founders = new_gen
    
    plt.plot(g,red,'r')
    plt.plot(g,purple, 'm')
    plt.plot(g,blue, 'b')
    plt.axis([0,gen,0,1.0])
    
    plt.show()

#sample_graph results
'''
[0.25, 0.4166666666666667, 0.3333333333333333]
[0.125, 0.625, 0.25]
[0.2916666666666667, 0.3125, 0.3958333333333333]
[0.25, 0.5208333333333334, 0.22916666666666666]
[0.3645833333333333, 0.359375, 0.2760416666666667]
[0.3802083333333333, 0.40625, 0.21354166666666666]
[0.3515625, 0.4661458333333333, 0.18229166666666666]
[0.416015625, 0.4069010416666667, 0.17708333333333334]
[0.453125, 0.3782552083333333, 0.16861979166666666]
[0.4568684895833333, 0.4052734375, 0.13785807291666666]
[0.4733072916666667, 0.3889973958333333, 0.1376953125]
[0.4820556640625, 0.3914388020833333, 0.12650553385416666]
[0.5002237955729166, 0.381591796875, 0.11818440755208333]
[0.5136006673177084, 0.3770650227864583, 0.10933430989583333]
[0.5244242350260416, 0.3763987223307292, 0.09917704264322917]
[0.5388692220052084, 0.36669667561848956, 0.09443410237630208]
[0.5502535502115885, 0.36140187581380206, 0.08834457397460938]
[0.5617383321126302, 0.35471343994140625, 0.08354822794596355]
[0.5715554555257162, 0.34991455078125, 0.07852999369303386]
[0.581236203511556, 0.34418853123982746, 0.07457526524861653]
'''   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    