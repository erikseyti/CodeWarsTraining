#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:52:48 2020

@author: erik
"""

def count(string):
    """
    Metodo que contabiliza a quantidade de caracteres de uma palavra e retorna um dicionario
    
    Entrada: uma string
    Saída: um dicionario numerico.
    
    Ex:
        count(aba) -> {'a': 2, 'b': 1}
    """
    dicionario_letras = {}
    for letra in string:
        if letra not in dicionario_letras:
            dicionario_letras[letra]=1
        else:
            dicionario_letras[letra]+=1
    return dicionario_letras