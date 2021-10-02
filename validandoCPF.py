#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  validandoCPF.py
class Util(object):
    #Classe util com metodo de validacao de cpf.
    def validaCpf(self,cpf,d1=0,d2=0,i=0):
        while i<10:
            d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
        return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))


#exemplo de uso

print Util().validaCpf("10006600956")

