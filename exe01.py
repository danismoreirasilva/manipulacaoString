nome = str(input('Digite o seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(nome.title())
print(f'Total de caracteres do nome: {len(nome)}')
print(f'Número de espaços no nome: {nome.count(" ")}')
print(len(nome) - nome.count(' '))
listaNome = nome.split()
print(listaNome[0])
#print(nome.split()[0]) outra forma sem criar a variável listaNome
print(f'{listaNome[0]} tem {len(listaNome[0])} letras.')

