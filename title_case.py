#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:07:48 2020

@author: erik
"""


def title_case(title, minor_words=''):
    """
    Metodo que converte o titulo de uma obra de forma Capitalizada.
    Com Exceção da primeira palavra do titulo, que será sempre capitalizada.
    
    Entrada: uma String com o titulo a ser convertido; uma string para indicar quais palavras não devem ficar capitalizados.
    Saída: Uma String.
    
    Exemplo:
        title_case('a clash of KINGS', 'a an the of') --> 'A Clash of Kings'
        
    
    """
    
    titulo = title.lower().split(" ")
    letras_minusculas = minor_words.lower().split(" ")    
    titulo_captalizado = titulo[0].capitalize()
    titulo.pop(0) 
    for palavra in titulo:
        if palavra in letras_minusculas:
            titulo_captalizado = titulo_captalizado + " "+ palavra
        else:
            titulo_captalizado = titulo_captalizado + " " + palavra.capitalize()    
    return titulo_captalizado