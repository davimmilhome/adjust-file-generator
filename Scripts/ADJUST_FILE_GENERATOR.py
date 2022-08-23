"""Esse código tem o propósito de formatar os
ajustes diretamente em arquivos, no caso, ele foi
desenvolvido como caso de estudo e tem de ser utilizado
do terminal, porém, pode ser adaptado."""
import sys
import os
import shutil as sh
import datetime as dt

#DEFININDO CLASSES DE ERRO
class Error(Exception):


	pass

class InputError(Error):


	def __init__(self,message):

		sel.message = message

#CRIANDO O ARQUIVO DE AJUSTE
# INFORMAÇÃO DA DATA ATUAL PARA NOMEAR O ARQUIVO
data_atual = dt.date.today().strftime('%d%m%Y')
nome_arquivo = f'ajuste{data_atual}.txt'
fo = open(nome_arquivo,'a')
fo.close()

#VARIÁVEIS
nu_cnpj = ''
nu_valor = ''
dt_data_mov = ''
dt_data_agd = ''
tp_ajuste = ''

path_out = input(r'Insira o caminho de saida do arquivo: ')

#Métodos
def f_ajuste_cnpj():
    global nu_cnpj



    nu_cnpj = input('Insira o CNPJ ou digite 0 para sair:\n')

    #Esse bloco retira pontos/traços/espaços do cnpj
    nu_cnpj = nu_cnpj.replace('.', '')
    nu_cnpj = nu_cnpj.replace('-', '')
    nu_cnpj = nu_cnpj.replace('/', '')
    nu_cnpj = nu_cnpj.replace(' ', '', -1)

    #Bloco de saída
    if nu_cnpj == '0':

        os.remove(nome_arquivo)
        sys.exit()

    #Checando se o CNPJ tem mais de 14 Caracteres
    elif len(nu_cnpj) > 14:

        print('Número inválido de carácteres\nPreencha novamente')
        f_ajuste_cnpj()

    #Confere 14 dígitos ao CNPJ (adição do zero inicial em alguns casos)
    while len(nu_cnpj) != 14:

        nu_cnpj = '0' + nu_cnpj

    # Esse bloco verifica se há carácteres não numéricos
    for i in nu_cnpj:

        try:

            type(eval(i))

        except:

            print('Não Numérico, preencha novamente.')
            f_ajuste_cnpj()

    #Bloco de encerramento
    print(f'O CNPJ de ajuste é: {nu_cnpj}')

def f_ajuste_valor():

    global nu_valor

    nu_valor = input('Insira o valor desejado com duas casas decimais:\n')

    # Esse bloco retira pontos/virgulas do valor
    nu_valor = nu_valor.replace('.', '')
    nu_valor = nu_valor.replace(',', '')
    nu_valor = nu_valor.replace(' ', '')

    #Bloco confere se o númere de carcteres é menor que três
    if len(nu_valor) < 3:

        print('Número insuficiente de carácteres\nPreencha novamente')
        f_ajuste_valor()

    # Esse bloco verifica se há carácteres não numéricos
    for i in nu_valor:

        try:

            type(eval(i))
        except:

            print('Não Numérico, preencha novamente.')
            f_ajuste_valor()

    #Bloco de encerramento
    print(
        f'O valor do ajuste é R$ '
        f'{nu_valor[:len(nu_valor)-2]+ "," + nu_valor[len(nu_valor)-2:]}')

def f_data_mov():
    global dt_data_mov


    dt_data_mov = input(
        'A data movimento (data ajuste) corresponde ao dia de'
        'hoje?\nDigite 1 para Sim ou 2 para Não\n')

    #Bloco que checa se a data movimento é a data atual
    if dt_data_mov == '1':

        dt_data_mov = data_atual

    #bloco onde o usuário escolhe digitar a data movimento
    elif dt_data_mov == '2':
        # Esse bloco retira pontos/traços/espaços da data movimento
        dt_data_mov = input('Insira a data movimento: dd/mm/aaaa\n')

        dt_data_mov = dt_data_mov.replace('.', '')
        dt_data_mov = dt_data_mov.replace('-', '')
        dt_data_mov = dt_data_mov.replace('/', '')
        dt_data_mov = dt_data_mov.replace(' ', '', -1)

    # checa se o número inserido é dieferente de 1, novamente
    else:

        if dt_data_mov == data_atual:

            pass

        else:

            print('Opção inválida, digite novamente.')
            f_data_mov()
            pass

    # Esse bloco verifica se há carácteres não numéricos
    for i in dt_data_mov:

            try:

                type(eval(i))

            except:

                print('Não Numérico, preencha novamente.')
                f_data_mov()
                break

    #Esse bloco checa se a data tem 8 caracteres
    if len(dt_data_mov) != 8:

        print('Número errado de carácteres\nPreencha novamente')
        f_data_mov()

def f_data_agd():
    global dt_data_agd


    dt_data_agd = input('Insira a data agendamento: dd/mm/aaaa\n')

    dt_data_agd = dt_data_agd.replace('.', '')
    dt_data_agd = dt_data_agd.replace('-', '')
    dt_data_agd = dt_data_agd.replace('/', '')
    dt_data_agd = dt_data_agd.replace(' ', '', -1)

    #Esse bloco checa se a data tem 8 caracteres
    if len(dt_data_agd) != 8:

        print('Data com o número errado de carácteres\nPreencha novamente')
        f_data_agd()

    #Esse bloco verifica se há carácteres não numéricos
    for i in dt_data_agd:

        try:

            type(eval(i))

        except:

            print('Não Numérico, preencha novamente.')
            f_data_agd()

    #Bloco de encerramento
    print(f'A data agendamento é: {dt_data_agd}')

def f_tp_ajuste():
    global tp_ajuste


    tp_ajuste = input('Qual o tipo de ajuste?\n1- Débito\n2- Crédito\n')
    lista_tipo_ajuste = ('1','2')

    #checa se o tipo de ajuste inserido faz sentido
    if tp_ajuste not in lista_tipo_ajuste:
        print('Opção inválida, digite novamente')
        f_tp_ajuste()

def f_edit_txt():

    #definindo a lista que será escrita no txt
    list_ajuste= ['D',nu_cnpj,nu_valor,dt_data_mov,dt_data_agd,tp_ajuste]
    string_ajuste = ';'.join(list_ajuste)
    print(f'Sua lista de valores é\n{list_ajuste}')
    #editando o txt
    fo = open(nome_arquivo, 'a')
    fo.write(f'{string_ajuste}\n')
    fo.close()

def f_new_ajuste():

    #Começando um novo ajuste
    new_ajuste = input(
        'Gostaria de adicionar um novo ajuste?\n1- Sim\n2- Não\n')

    if new_ajuste == '1':

        f_ajuste_geral()

    elif new_ajuste == '2':

        sh.copy(nome_arquivo, path_out)
        os.remove(nome_arquivo)

    else:

        print('Opção inválida.')
        f_new_ajuste()


def f_ajuste_geral():

    #Executando as funções
    f_ajuste_cnpj()
    f_ajuste_valor()
    f_data_mov()
    f_data_agd()
    f_tp_ajuste()
    f_edit_txt()
    f_new_ajuste()

if __name__ == '__main__':

    f_ajuste_geral()
