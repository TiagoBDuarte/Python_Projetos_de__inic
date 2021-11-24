#Escreva um programa que leia dois números. Imprima o resultado da 
#multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e 
#subtração para calcular o resultado.

a=int(input('Digite o valor do primeiro número:'))
b=int(input('Digite o valor do segundo número:'))
x=1
y=0
while x<b:
    y=y+a
    x=x+1    
    print(f'{a} x {b} = {y}')
