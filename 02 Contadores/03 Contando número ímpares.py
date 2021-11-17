#Contando número ímpares
fim=int(input('Digite que irá terminar: '))
x=1
while x<=fim:
    x=x+2
    if x>fim or x%fim==0:
        x=x-1
    else: print(x)