#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia
#da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver
#o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão
#informado pelo usuário, conforme o exemplo abaixo:

y=float(input("Digite o valor da unidade do pão: "))
x=1
while x<=50:
    preço= y * x
    x=x+1
    print(f'Com o valor de {y:5.2f} a unidade(s){x} é {preço:5.2f}')