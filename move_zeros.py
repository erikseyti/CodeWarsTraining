#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:17:25 2020

@author: erik
"""

import pdb

def move_zeros(array):
    contadorZeros = 0
    # pdb.set_trace()
    
    for elemento in array:
        print(type(elemento))
        if elemento == type(bool):
            print(elemento)
            continue
            # array.remove(elemento)
            
        elif elemento is 0.0 or elemento is 0 and type(int):
            print(elemento)
            array.pop(elemento)
            contadorZeros = contadorZeros + 1
    
    # print(contadorZeros)
    # print(array)
    
    for zero in range(contadorZeros):
        array.append(0)        
    
    
    
    #your code here
    print(array)
    
    
    

    
    
    
move_zeros([0,1,None,2,False,1,0])

move_zeros([False,0,1])    

move_zeros([1,2,0,1,0,1,0,3,0,1])
