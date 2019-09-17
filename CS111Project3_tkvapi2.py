# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:26:46 2017

@author: kvapil98
"""


def list_ancestors(tax,dic):
    '''lists all the ancestors of a species'''
    par = []
    par.append(tax)
    for i in dic:
        if tax not in dic:
            return par
        if dic[tax] in dic:
            par.append(dic[tax])
            tax = dic[tax]
        else:
            par.append(dic[tax])
            return par

def root(dic):
    '''Finds the root of the tree'''
    keys = []
    for tax in dic.keys():
        keys.append(tax)
    #print(keys)
    ancestors = list_ancestors(keys[0],dic)
    return ancestors[-1]

def kids(tax,tree):
    '''returns the younger species'''
    taxa = []
    for i in tree:
        if tree[i] == tax:
            taxa.append(i)
    return taxa

def common_ancestor(listax,dic):
    '''finds common ancestor of species'''
    total = []
    common = []
    counter = 1
    for key in listax:
        total.append(list_ancestors(key,dic))
    while counter <= len(total):
        for key in range(len(total[0])):
            if total[0][key] in total[counter-1]:
                common.append(total[0][key])
        counter += 1
    for key in common:
        if common.count(key) == len(total):
            return key
    if common == []:
        return []

def c_ancestor(listax,dic):
   '''finds ancestors with special name inputs'''
   new_name = {}
   for key in dic:
       new_name[key] = dic[key]
       if ' ' in key:
           period = key[0] + '.'
           space = key.find(' ')
           total = period + ' ' + key[space + 1:]
           new_name[total] = dic[key]
   return common_ancestor(listax, new_name)
