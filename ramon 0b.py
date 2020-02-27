#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 0b

#Entregar por e-mail para marcoandre@ifc-araquari.edu.br
#com o assunto: prg2: lista0b.
#Envie um arquivo zip com o nome no formato seu_nome.zip.

#1. Crie uma função que leia um endereço IP no formato a.b.c.d e retorne
# se ele é ou não um IP válido.
a = open('ips.txt' , 'r')
for x in a:
    if x >= 256:
        print ("ip é não é valido %s" %x)
    else:
        print ("Ip é válido %s"%x)

#2. Faça um programa que leia um arquivo contendo uma lista de endereços
#IP no formato a.b.c.d e gere um arquivo com os IPs válidos e outro com
#os IPs inválidos.
b = open ("ips.txt")
print b
for i in len (b):

#3. Faça um programa que leia os três arquivos com os IPs e crie uma
#página HTML básica, contendo a lista completa desses IPs,
#e depois a lista dos válidos e inválidos.

#4. Faça um programa que leia o arquivo alice.txt
#(ou outro arquivo semelhante à sua escolha)
#e mostre as dez palavras que aparecem com mais frequência no texto
