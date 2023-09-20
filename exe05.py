nome = str(input('Digite o nome completo: ')).strip().title()
print(f'O primeiro nome é: {nome.split()[0]}')
print(f'O último nome é: {nome.split()[-1]}')
