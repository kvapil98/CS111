# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:25:10 2017

@author: kvapi
"""








def get_dna(dna):
    print('The total length of the gene is', len(dna))
    print("There are", dna.count('A'), "A's")
    print("There are", dna.count('T'), "T's")
    print("There are", dna.count('G'), "G's")
    print("There are", dna.count('C'), "C's")
    per_A = (dna.count('A') / len(dna)) * 100
    print("%A=", round(per_A, 1))
    per_T = (dna.count('T') / len(dna)) * 100
    print("%T=", round(per_T, 1))
    per_G = (dna.count('G') / len(dna)) * 100
    print("%G=", round(per_G, 1))
    per_C = (dna.count('C') / len(dna)) * 100
    print("%C=", round(per_C, 1))
    amino = len(dna[::3])
    print("Number of amino acids=", amino)
    

sample_dna = 'ACGTT'
get_dna(sample_dna)

        
        
        
        
        
        