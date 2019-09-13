# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:17:14 2019

@author: Carol
"""
salario = int(input("digite seu salario: "))
aumento = float(input('Digite seu aumento em %: '))

print ("Seu aumento foi...", ((salario*aumento)/100))
print ('Seu novo salario eh: ', (((salario*aumento)/100)+salario) )