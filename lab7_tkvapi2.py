# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:30:09 2017

@author: kvapil98
"""
def get_orf(dna):
    '''this func gets orf strating with ATG end in but dont include stop codon'''
    cod = -3
    while cod < len(dna):
        cod +=3
        codon = dna[cod:cod+3]
        if codon in ['TGA','TAG','TAA']:
            return dna[:cod]
    return(dna)


def read_seq(file, seq):
    count = 0
    synth = open(file,'r' )
    for line in synth:
        if line.count('>') == 1:
            count += 1
        if count == seq + 1:
            synth.close()
        if line.count('>') != 1:
           print(line, end='')
           print(len(line))
           
           
def read_seq1(file, seq):
    '''This func takes the file and puts the sequences blocked together for how many sequences'''
    count = 0
    synth = open(file,'r' )
    for line in synth:
        if line.count('>') == 1:
            count += 1
        if count == seq + 1:
            synth.close()
        if line.count('>') != 1:
            print(line, end='')

#I was not able to create the list put I did do the first part
#The function prints out the seqeuinces and it works when you put in how many
           
         
            
    
    