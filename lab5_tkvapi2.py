# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:20:36 2017

@author: kvapil98
"""

DNA = 'ACGATGACAGTAC'
mRNA = 'ACGATGACAGTAAGC'


def comp_nuc(base, seq):
   '''This func takes the complement base of DNA or mRNA'''
   if base == 'A' and seq == DNA:
        return 'T'
   if base == 'A' and seq == mRNA:
        return 'U'
   if base == 'T' and (seq == DNA or seq == mRNA):
        return 'A'
   if base == 'G' and (seq == DNA or seq == mRNA):
        return 'C'
   if base == 'C' and (seq == DNA or seq == mRNA):
        return 'G'
    
def comp_to_dna(seq):
    '''This func takes the complement of DNA'''
    comp_DNA = ''
    for i in seq:
        comp_DNA += comp_nuc(i, DNA)
    return comp_DNA


def comp_to_rna(comp_DNA):
    '''This func takes the 3'-5' DNA and creates 5'-3' mRNA'''
    comp_to_rna = ''
    for i in comp_DNA:
        comp_to_rna += comp_nuc(i, mRNA)
    return comp_to_rna

def gc_content(seq):
    '''This func returns the fraction of G and C in DNA'''
    num_g = seq.count('G')
    num_c = seq.count('C')
    tot_gc = num_c + num_g
    fract_gc = tot_gc / len(seq)
    return fract_gc