#desenvolva um programa de correção de gabarito com com respostas em letras maiusculas e minusculas.
#terminando projeto
pontos=0
print('Questão 1- Qual foi o ano da primeira constituição da história do Brasil:')
print('A - 1937')
print('B - 1934')
print('C - 1824')
print('D - 1988')
resposta=input()
if resposta == 'C' or resposta=='c':
     pontos=pontos+1
        
print('Questão 2 - foi líder e mártir da Confederação do Equador (1824).')
print('A - Getúlio Vargas')
print('B - D.Pedro II')
print('C - Frei Caneca')
print('D - Tomé de Souza')
resposta=input()
if resposta == 'C' or resposta=='c':
     pontos=pontos+1
         
print('Questão 3 - A revolta, ocorrida em Salvador, capital da Bahia, que aconteceu na noite de 24 para 25 de janeiro de 1835, foi o maior levante de escravizados negros de origem islâmica foi a: ')
print('A - Revolta dos Malês')
print('B - Revolta da Chibata')
print('C - Revoltas Estudantis')
print('D - Revolta dos 18 do Forte')
resposta=input()
if resposta == 'A' or resposta=='a':
    pontos=pontos+1
if pontos >=2:
    print(f'Sua pontuação foi de {pontos} e está aprovado')
else:
    print(f'Sua pontuação foi de {pontos} e está reprovado')

    