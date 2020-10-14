# Agora devemos filtrar os tipos de imóveis de acordo com os seguintes requerimentos.

# 1)Selecione somente os imóveis classificados com tipo 'Apartamento'.
# 2)Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
# 3)Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
# 4)Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.

import pandas as pd

dados = pd.read_csv('aluguel.csv', sep = ';')
print(' ')
print('DADOS DO ARQUVIO ORIGINAL:')
print(dados.head(10))


# Imóveis classificados com tipo 'Apartamento'.

selecao_apartamentos = dados['Tipo'] == 'Apartamento'
frequencia_n1 = dados[selecao_apartamentos].shape[0]


# Imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.

selecao_casas = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
frequencia_n2 = dados[selecao_casas].shape[0]


# Imóveis com área entre 60 e 100 metros quadrados, incluindo os limites

selecao_area = (dados['Area'] >= 60) & (dados['Area'] <= 100)
frequencia_n3 = dados[selecao_area].shape[0]


# Imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.

selecao_quartos_aluguel = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
frequencia_n4 = dados[selecao_quartos_aluguel].shape[0]

print('1 - Nº de imóveis classificados com tipo "Apartamento" - {}'.format(frequencia_n1))
print('2 - Nº de imóveis classificados com tipo "Casa", "Casa de Condomínio" e "Casa de Vila" - {}'.format(frequencia_n2))
print('3 - Nº de imóveis classificados com área entre 60 e 100 metros quadrados, incluindo os limites - {}'.format(frequencia_n3))
print('4 - Nº de imóveis classificados que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 - {}'.format(frequencia_n4))

