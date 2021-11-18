#Escolha sua próxima tabuada do início ao fim.
print('Selecione as opções de tabuada:')
tabuada=int(input('Digite qual tabuada deseja os resultados: '))
início=int(input('Digite o início da tabuada: '))
fim=int(input('Digite o fim da tabuada: '))
 
while início<=fim:
    if tabuada==0:
        while início<=fim:
            print(f'{tabuada} x {início} = {tabuada}')
            início=início+1
    elif início == 0 and início <= fim:
        print(f'{tabuada} x {início} = {tabuada*início}')
        
    else:    print(f'{tabuada} x {início} = {início*tabuada}')
    início=início+1