#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:23:59 2020

@author: erik
"""


def alphabet_position(text):
    
    dicionario_alfabetico = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26"}
    text = text.lower()
    texto_em_numeros = ""    
    for letra in text:
        if letra in dicionario_alfabetico:
            numero_letra = dicionario_alfabetico.get(letra)
            texto_em_numeros = texto_em_numeros + numero_letra + " "            
    texto_em_numeros = texto_em_numeros[:-1]
    return texto_em_numeros


