#Altere o programa anterior de forma a perguntar também o valor 
#depositado mensalmente. Esse valor será depositado no início de cada mês, e você 
#deve considerá-lo para o cálculo de juros do mês seguinte.

ativo = float(input("Insira valor inicial : "))
taxa = float(input('Digite a taxa: '))
ativo_2 =float(input('Insira o valor mensal: '))
mês = 1
lucro = ativo
while mês <= 3:
       lucro = (lucro + (lucro*(taxa/100))+ ativo_2 )
       print(f'No mês {mês} o saldo é {lucro:5.2f}')
       mês= mês + 1       
print(f'O seu investimento foi de R${ativo:5.2f} e o lucro de R${lucro-ativo:5.2f}.')
        