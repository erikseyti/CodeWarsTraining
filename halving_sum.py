#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:32:39 2020

@author: erik
"""


def halving_sum(n):
    """
    Metodo que realiza uma soma a partir de um numero n, e a cada interação soma-se metade do valor de n até chegar a 0 ou 1.
    
    Entrada: um Int.
    Saída: um Int.
    
    Ex:
        halving_sum(25) --> 47.
    """
    soma = n
    valorAtual = n
    while True:        
        valorAtual = int(valorAtual/2)
        soma = soma + valorAtual
        if valorAtual == 1 or valorAtual == 0:
            break        
    return soma
