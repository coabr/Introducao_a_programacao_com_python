# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:17:14 2019

@author: Carol
"""
km_perc = int (input('km?'))
dias = int (input('dias?'))

diaria = 60.0
rodagem = 0.15

preco = (km_perc * rodagem) + (dias * diaria)

print (preco)