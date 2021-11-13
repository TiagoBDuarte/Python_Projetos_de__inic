#Escreva um programa que pergunte o valor inicial de uma dívida e 
#o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número 
#de meses para que a dívida seja paga, o total pago e o total de juros pago.

dívida= float(input('Insira o valor da sua dívida: '))
juros_dívida= float(input('Juros Mensais(Exemplo se digite 3 logo 3%: '))
cred_mensal =float(input('Digite o valor mensal a ser pago: '))
qtm= float(input('Em quantos meses:'))
dívida_m = (dívida+(juros_dívida/100))/qtm

if cred_mensal < dívida_m:
    print('Valor mensal inválido para quitação valor menos que a dívida, informe')
    print(f'um valor maior ou igual a R${dívida_m:5.2f} ')