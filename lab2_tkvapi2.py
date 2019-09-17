# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:11:01 2017

@author: kvapi
"""

a = 510 #part 1
t = 986
c = 798
d = 854
total_count = a + t + c + d

print('The total length of the DNA string is', end=' ')
print(total_count)

def get_codon(dna): #part 2
    print(dna[0:3])
    
get_codon('CGTAGCTGCAGT')