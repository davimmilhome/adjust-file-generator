import pandas as pd, datetime as dt, os
import csv

#VARIABLES AND PATH TO DEFINE FILES
actual_date = dt.date.today().strftime('%d%m%Y')
file_name = f'\\ajuste{actual_date}.txt'

path_in = input(r"""Insira o caminho do arquivo CSV
Ex: .../Área de Trabalho\Organização\ARQUIVO_AJUSTE\arquivo.csv
Certifique-se de que o arquivo está no formato de [CNPJ,VALOR,DATA_AGENDAMENTO,TIPO_AJUSTE] e SEM CABEÇALHO
Certifique-se de que o valor foi colocado contendo duas casas decimais (centavos) EX: 0,40 ou 5,39 ou 598,28
Os carácteres contidos nessa lista serão removidos: ['.',',','-','/']
- """)  #LIST OF CARACTHERS DOES NOTE UPDATE AUTOMATICALLY, LOOK AT REGEX LINE

path_out = input(r"""Insira o caminho de saida do arquivo
Ex: .../Área de Trabalho\Organização\ARQUIVO_AJUSTE
- """)

#READING DF
df = pd.read_csv(
            path_in,
            header=None,
            on_bad_lines='skip',
            delimiter=';',
            decimal=','
)

#FORMATING COLUMNS
df.columns = headers = [
    'CNPJ',
    'VALUE',
    'SCHEDULE_DATE', #DATA AGENDAMENTO
    'ADJUST_TYPE'
]

#CREATING NEW COLUMNS  - REORDERING  - REGEX

df['ADJUST_DATE'] = actual_date
df['D']           = 'D'

df = df.reindex(columns=['D','CNPJ','VALUE','ADJUST_DATE','SCHEDULE_DATE','ADJUST_TYPE'])
df = df.astype(str, errors='ignore')

df.replace({'-':'','\/':'','\.':'','\,':''},inplace= True,regex = True)

#FORMATING CNPJ
def CNPJ_form(x):
    while len(x) != 14:
        x = '0'+x
    if len(x) == 14:
        return x

df['CNPJ'] = df['CNPJ'].map(lambda x: CNPJ_form(x))


#GENERATING TXT FILE
df.to_csv(path_out + file_name, sep=';', header=False, index=False)


if __name__ == '__main__':
    print(df.to_string())
    pass