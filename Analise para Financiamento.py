""" Escreva um programa para analise de emprestimo bancario para compra de uma casa
O programa deve perguntar o valor do imovel, o salario e o periodo para pagamento
E diga se ele pode ou não compra a casa - 30% da renda."""

from time import sleep
nome = input("Bem-vindo. Por favor, nos diga seu nome: ")
CPF = input('Digite seu CPF, utilizando somente números:')
print('É um prazer recebe-ló.\nPor favor, insira as informações abaixo para analise de seu emprestimo')
vi = float(input('Valor do imóvel: R$'))
ve = float(input('Valor de entrada: R$'))
if ve < ((20/100)*vi):
    print('O valor de entrada esta abaixo do percentual exigido para o valor informado.')
    print('Infelizmente não poderemos prosseguir com sua analise.')
    exit()
else:
    r = float(input('Renda total: R$'))
    t = int(input('Prazo de pagamento, em meses:'))
    p = vi / t
    l = ((30/100)*r)
    print('Analisando sua proposta...')
sleep(3)
if p == l or p > l:
    print('O valor da parcela será de R${:.2f}, ultrapassando 30% sua renda total. \nInfelizmente seu crédito não aprovado'.format(p))
else:
    print('Valor da parcela será de R${:.2f}. Parabéns, seu emprestimo foi aprovado!'.format(p))