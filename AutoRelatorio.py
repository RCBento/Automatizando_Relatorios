import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#indica o arquivo excel já criado
arquivo_excel = 'TabVendas.xlsx'

#variaveis que salva o conteúdo das sheets da planilha do excel
tb_1 = pd.read_excel(arquivo_excel,sheet_name='Tabela1')
tb_2 = pd.read_excel(arquivo_excel,sheet_name='Tabela2')
tb_3 = pd.read_excel(arquivo_excel,sheet_name='Tabela3')

#variavel que concatena todas as variaveis criadas acima
tb_consolidada = pd.concat([tb_1,tb_2,tb_3])

#salva o arquivo em excel consolidado
tb_consolidada.to_excel('RelVendas.xlsx')

#variavel que agrupa/classifica por uma coluna e soma
total_vendas = tb_consolidada.groupby(['Vendedor']).sum()

#variavel que organiza o agrupamento realizado antes e limpa de acordo com as colunas selecionadas
relatorio_final = total_vendas.loc[:,"Quantidade":"Preço Unitário"]

print(relatorio_final)

#criação do gráfico em barras
relatorio_final.plot(kind='bar')
plt.show()