#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sem título.py
arquivo = open ("numeros.txt" , "w")
entrada = arquivo.readlines()
arquivo.close()

soma = 0
for linha in enumerate (entrada):
    numero = numero.strip()
    if not numero : continue
    try:
        soma += int(numero)
    except:
        print ("Erro na linha #%d: [%s]" % (i,numero))

arquivo_saida = open ("soma.txt" , "w")
arquivo_saida.write("%s\n" %soma)
arquivo_saida.close()


#Separar Email
entrada = open ("optativas.csv" , "r")
votos = entrada.readlines()
entrada.close()
saida_lisa = []
for linha in votos [1:]:
    aluno  = linha.split(',')
    print('"%s"<%s>'  %(aluno [1] , aluno[2]))

saida = open ("contatos.txt" , "w")
saida.writelines (saida_lista)
saida.close()
    
    

#extend usa para chamar a lista completa , e uma sublista , até uma sublista: Exemplo disciplinas.extend(aluno[-3:])
