# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:13:38 2017

@author: kvapil98
"""
#part 1 example: orf_advisor('ATGATAG') >>> 'The string is not of the correct length.'
#part 2 example: codon_finder(mrna) >>> 
#The codons ['AUG', 'GCC', 'GGA', 'AUA', 'UGU', 'UAA'] make a protein that is MAGIC .
#returns list: ['AUG', 'GCC', 'GGA', 'AUA', 'UGU', 'UAA']


def orf_advisor(dna):
    '''This function finds if the sequence is an ORF'''
                
    if dna[0:3] != 'ATG':
        return 'The first three bases are not ATG.'
    elif dna[-3:] != 'TAG' and dna[-3:] != 'TAA' and dna[-3:] != 'TGA':
        return 'The last three bases are not a stop codon.'
    elif len(dna) % 3 != 0:
        return 'The string is not of the correct length.'
    else:
        return 'This is an ORF'


#used the following to find the reverse of the mrna sequence that was given
mrna = 'UGUAUAAGGCCGAGG'
mrna = mrna[::-1]

def codon_finder(mrna):
    '''This function finds codons and protein sequence for given mrna'''
    
    my_list = [mrna[0:3], mrna[3:6], mrna[6:9], mrna[9:12], mrna[12:15]]
    my_list[0] = 'AUG'
    my_list.append('UAA')
    pro_codes = 'MAGIC'
    print('The codons', my_list, 'make a protein that is', pro_codes,'.')
    return my_list

