#Realatório e Análise I
#Importando a base de dados

import pandas as pd

dados_aluguel = pd.read_csv('aluguel.csv', sep = ';')

#print(dados_aluguel.head())
#print(' ')

#Tipos de dados no arquivo
tipos_de_dado = pd.DataFrame(dados_aluguel.dtypes, columns = ['Tipos de Dados'])
tipos_de_dado.columns.name = 'Variáveis'
print(tipos_de_dado)
print(' ')
print('A base de dados possui {} registros e {} variáveis'.format(dados_aluguel.shape[0], dados_aluguel.shape[1]))





