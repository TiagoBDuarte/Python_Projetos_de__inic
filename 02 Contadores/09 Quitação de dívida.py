#Sistema de quitação de dívida
dívida=float(input('Digite o valor inicial da dívida:'))
taxa = float(input('Digite a taxa de juros:'))
pag_mensal=float(input('Digite o valor do pagamento mensal:'))
quitação=dívida
juros=(dívida*(taxa/100))
x=0
if pag_mensal<= juros:
    print(f'Seu pagamento mensal é menos que os juros, insira um valor maior')
else:
    while quitação>0:
        quitação= quitação + juros - pag_mensal
        x=x+1
        print(f'O valor pago no mês{1} foi de R${pag_mensal:5.2f} e sua dívida ficou em R${quitação:5.2f}')  
        print(f'Sua dívida de R${dívida:5.2f} foi quitada')
