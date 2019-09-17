# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:06:46 2017

@author: kvapil98
"""

# copy and pasted this function from lab #7
def get_orf(dna):
    '''this func finds orf when dna starts with ATG and ends in but doesnt include stop codon'''
    cod = -3 #started with - 3 to account for the early counter change
    while cod < len(dna):
        cod +=3
        codon = dna[cod:cod+3]
        if codon in ['TGA','TAG','TAA']: #cuts off the stop codon from final dna
            return dna[:cod]
    return(dna)

def one_frame(dna):
    '''This func outputs a list of the orfs in inputted sequence'''
    nuc = -3 #started with -3 to account for early counter change
    orf_list = [] #template for final list
    while nuc < len(dna):
        nuc += 3
        if dna[nuc:nuc+3] == 'ATG':
            orf_list.append(get_orf(dna[nuc:])) #calls get_orf when finds 'ATG'
            nuc = nuc+len(get_orf(dna[nuc:]))  #this length accounts for the length of the orf and adds to origanl
    return orf_list


def find_all_orfs(dna):
    '''This func finds all the possible orfs in a sequence places them all in one list'''
    total_list = [] #created to be used as template for final list
    slic = 0 
    while slic < 3:
        total_list.extend(one_frame(dna[slic:])) #used extend to have only one list of all the orfs
        slic += 1
    return total_list

# copy and pasted this function from lab#5
def gc_content(seq):
    '''This func returns the fraction of G and C in DNA'''
    num_g = seq.count('G')
    num_c = seq.count('C')
    tot_gc = num_c + num_g
    fract_gc = tot_gc / len(seq)
    return fract_gc

def gene_finder(file_name, min_len, minGC):
      '''this func takes all the orfs in a given file with the given requirements''' 
      final_list = []
      sal = open(file_name, 'r')
      contents = sal.read()
      orf = find_all_orfs(contents)
      index = 0
      for seq in orf: #for each sequence in that list
          if (len(orf[index]) >= min_len) and (gc_content(orf[index]) >= minGC): #parameter requirments
              one_list = [] #created to be added in the final list
              one_list.append(seq)
              one_list.append(len(seq))
              one_list.append(gc_content(seq))
              final_list.append(one_list)
              #print(index)
          index += 1
      sal.close()
      print(final_list)

#when I ran the gene_finder, I found a total of 63 genes
#'Best Gene': ['ATGGGCATTTTTGCCTCCGCAGGATGCGGTAAGACCATGCTGATGCATATGCTGATCGAGCAAACGGAGGCGGATGTCTTTGTTATCGGTCTTATCGGTGAACGAGGCCGTGAGGTCACTGAATTCGTGGATATGTTGCGCGCTTCGCATAAGAAAGAAAAATGCGTGCTGGTTTTTGCCACTTCCGATTTCCCCTCGGTCGATCGCTGCAATGCGGCGCAACTGGCGACAACCGTAGCGGAATATTTTCGCGACCAGGGAAAACGGGTCGTGCTTTTTATCGATTCCATGACCCGTTATGCGCGTGCTTTGCGAGACGTGGCACTGGCGTCGGGAGAGCGTCCGGCTCGTCGAGGTTATCCCGCCTCCGTATTCGATAATTTGCCCCGCTTGCTGGAACGCCCAGGGGCGACCAGCGAGGGAAGCATTACTGCCTTTTATACGGTACTGCTGGAAAGCGAGGAAGAGGCGGACCCGATGGCGGATGAAATTCGCTCTATCCTTGACGGTCACCTGTATCTGAGCAGAAAGCTGGCCGGGCAGGGACATTACCCGGCAATCGATGTACTGAAAAGCGTAAGCCGCGTTTTTGGACAAGTCACGACGCCGACACATGCTGAACAGGCATCTGCCGTGCGTAAATTAATGACGCGTTTGGAAGAGCTCCAGCTTTTCATTGACTTGGGAGAATATCGTCCTGGCGAAAATATCGATAACGATCGGGCGATGCAGATGCGGGATAGCCTGAAAGCCTGGTTATGCCAGCCGGTAGCGCAGTATTCATCCTTTGATGACACGTTGAGCGGTATGAATGCATTCGCTGACCAGAAT', 831, 0.5342960288808665]
#The source from my gene is from a bacteria named  Salmonella enterica
#This protein is a family type III secretionsystem ATPase
#The protein has both molecular function and is invlolved in biological prcoesses
#Molecular Function: ATPase activity and ATP binding
#Biological Prcoesses: ATP metabolic process, biosynthetic process, proton transport, and protein secretion
# length: 831
# GC content: 0.534  
