from sys import stdin

mydict = dict()

for line in stdin:
	key, value, = line.split()
	mydict[key] = value

mylist = set()

for key in stdin:
	key = key[:-1]
	if key in mydict.keys():
		mylist.add(key)

"""
Utilizei duas variáveis globais mydict e mylist, respectivamente, a lista de dicionários e
um set (estrutura de dados não ordenada, mutável e que não armazena elementos repetidos).

Inicialmente, inicializei a lista de dicionários, li seus valores até EOF e os armazenei na estrutura de dados.
Em seguida, inicializei a segunda lista e li novamente até EOF, dessa vez, removendo o último char ('\n') ao invés de usar split.
Logo abaixo dessa operação, foi verificado se a chave estava no dicionário e, caso estivesse, adicionava na segunda lista.
"""
