#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:15:11 2020

@author: erik
"""


def odd_or_even(arr):
    soma = 0
    for n in arr:
        soma = soma + n    
    resto = soma % 2
    if resto == 0:
        return "even"
    return "odd"
