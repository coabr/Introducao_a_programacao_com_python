# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:17:14 2019

@author: Carol
"""
cigarros = int(input('cigarros hoje?'))
anos = int(input('anos fumando?'))

tempo = (cigarros * 10)

print ('voce perdeu %f  dias de vida' % tempo/60/24)