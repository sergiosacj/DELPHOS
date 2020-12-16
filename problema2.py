from pandas import read_csv

def sort_list(fileName):
	dataframe = read_csv(fileName+'.csv', delimiter=';')

	rowsList = [list(row) for row in dataframe.values]
	rowsList.sort(key=lambda column:column[2])
	# rowsList.insert(0, dataframe.columns.to_list())

	return rowsList

fileName = input("Nome do arquivo csv: ")
print(sort_list(fileName))

"""
Utilizando a biblioteca de dados pandas, li o arquivo csv e armazenei em um
dataframe, que é uma estrutura de dados fornecida pela biblioteca pandas.

Em seguida, criei uma lista de listas a partir desse dataframe. É importante ressaltar que
essa lista de listas não possui a primeira linha do arquivo csv, já que é apenas o header.
Caso fosse necessário adicionar o header, bastaria descomentar a linha 7 que adiciona todas
as colunas 0, ou seja, todo o header.

Por fim, na ordenação, é utilizada uma função lambda para definir os critérios de ordenação.
Foi definido apenas o critério exigido, mas poderiam ser definidos vários critérios.
"""
