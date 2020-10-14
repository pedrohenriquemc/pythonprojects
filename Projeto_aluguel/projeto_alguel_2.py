#Trabalhando com "series"
#Aqui vamos filtras a coluna ' Tipos " para exibir os tipos únicos de imóveis que nosso documento possui

import pandas as pd

dados_aluguel = pd.read_csv('aluguel.csv', sep = ';')

#FAzendo uma série com a coluna "Tipo"
tipos_de_imovel = dados_aluguel['Tipo']
print(" ")

#Deixando cada tipo único de imóvel na série
tipos_de_imovel.drop_duplicates(keep = 'first', inplace=True)

#Criando o Data Frame
tipos_de_imovel = pd.DataFrame(tipos_de_imovel)

#Mudando o Index do Data Frame
tipos_de_imovel.index = range(len(tipos_de_imovel))

#Nomeando a primeira coluna
tipos_de_imovel.columns.name = 'Id'
print(tipos_de_imovel)
