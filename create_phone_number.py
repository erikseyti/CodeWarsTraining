#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:03:06 2020

@author: erik
"""

def create_phone_number(n):    
    numero_telefone = "("
    contador = 0
    for numero in n:
        numero_telefone = numero_telefone + str(numero)
        if contador == 2:
            numero_telefone = numero_telefone + ") "
        if contador == 5:
            numero_telefone = numero_telefone + "-"
        contador = contador + 1
    return numero_telefone