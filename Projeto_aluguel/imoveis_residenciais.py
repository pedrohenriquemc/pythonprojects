#Agora devemos filtrar a nossa lista de forma que contenha apenas ióveis do tipo residencial

import pandas as pd

#Importando o documento
dados = pd.read_csv('aluguel.csv', sep = ';')
print(dados.head(10))

print(' ')
print(' Tipos de imóveis presentes no documento ')

#Tipos de imóveis presentes no documento
print(list(dados['Tipo'].drop_duplicates()))

print(' ')
print(' ')

#Criando uma lista apenas com o tipo que desejamos
print(" Itens cosiderados para a lista de 'Residenciais'")
lista_redisdencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']
print(lista_redisdencial)

print(' ')
print(' ')

#Filtrando o Data Frame original
selecao = dados['Tipo'].isin(lista_redisdencial)

#Aplicando a filtragem ao Data Frame original
dados_residencial = dados[selecao]
dados_residencial.index = range(len(dados_residencial))
print(dados_residencial)
print('Temos um total de {} linhas'.format(dados_residencial.shape[0]))
