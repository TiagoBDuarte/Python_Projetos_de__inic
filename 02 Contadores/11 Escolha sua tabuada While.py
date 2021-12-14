while True:
    print('Selecione a tabuada\nAdição - 1\nSubtração - 2\nMultiplicação - 3\nDivisão - 4')
    opcao = int(input('Escolha a tabuada aritmética ou zero para sair: '))
    if opcao == 0:
        break
    
    if opcao == 1:
        tabuada = int(input('Digite a tabuada de soma: '))
        numero = 0
        while numero <= 10:
            print(f'{tabuada} + {numero} = {tabuada + numero}')
            numero += 1
    elif opcao == 2:
        tabuada = int(input('Digite a tabuada de subtração: '))
        numero = 0
        while numero <= 10:
            print(f'{tabuada} - {numero} = {tabuada - numero}')
            numero += 1
            
    elif opcao == 3:
        tabuada = int(input('Digite a tabuada de multiplicação: '))
        numero = 0
        while numero <= 10:
            print(f'{tabuada} x {numero} = {tabuada * numero}')
            numero += 1
            
    elif opcao == 4:
        print('Não existe divisão por zero nos numeros reais')
        tabuada = int(input('Digite a tabuada de divisão: '))
        numero = 1
        while numero <= 10:
            print(f'{tabuada} / {numero} = {tabuada / numero}')
            numero += 1
    
    
