#Escreva um programa que pergunte o depósito inicial e a taxa de 
#juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
#Escreva o total ganho com juros no período. 
Ativo = float(input("Insira o valor do ativo: "))
taxa = float(input('Digite a taxa: '))
mês = 1
Lucro = Ativo
while mês <= 3:
       Lucro = (Lucro + (Lucro*(taxa/100)))
       print(f'No mês {mês} o saldo é {Lucro:5.2f}')
       mês= mês + 1       
       print(f'O seu investimento foi de R${Ativo:5.2f} e o lucro de R${Lucro-Ativo:5.2f}.')