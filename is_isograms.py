#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:20:24 2020

@author: erik
"""


def is_isogram(string):
    """
    Metodo que determina se uma serie de caracteres possui caracteres não possuem caracteres repetidos.
    Um termo "Isograma"
    
    Entrada: uma string.
    Saída: Um valor Booleano.
    
    Ex:
        is_isogram("aba") --> False
    """
    dicionario_alfabetico = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for letra in string.lower():
        if letra in dicionario_alfabetico:
            dicionario_alfabetico[letra] +=1
            if dicionario_alfabetico[letra] > 1:
                return False
    return True
            