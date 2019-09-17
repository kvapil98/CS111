# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:22:21 2017

@author: kvapil98
"""

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}



def translate_dna(dna):
    '''translates dna sequence into protein sequence'''
    new = dna.upper()
    pro_dna = ''
    og_start = new.find('ATG')
    if og_start == -1:
        og_start = 0
    start = new.find('ATG')
    if start == -1:
        start = 0
    for i in range(int(len(new[og_start:])//3)):
        key = new[start:start+3]
        if key not in gencode:
            pro_dna += 'X'
        else:
            pro_dna += gencode.get(key)
        start += 3
    return pro_dna
        
#Accession code: LX064076.1
#DNA Sequence: GCAGCACCCCGGAACCAGAGAGAGGATTAGCCTTTTTTTTTTTTTTTCTGTCGCATCGAGAG
#Protein Sequence: 'AAPRNQRED_PFFFFFCRIE'

def translate_reverse(dna):
    '''Reverses a dna sequence and find the protein sequence'''
    new = dna.upper()
    new = new.replace('A','a')
    new = new.replace('C','c')
    rev = new.replace('T','A')
    rev = rev.replace('a','T')
    rev = rev.replace('G','C')
    rev = rev.replace('c', 'G')
    return translate_dna(rev)

#Protein sequnce for Accession code: 'RRGALVSLLIGKKKKKTA_L'
















