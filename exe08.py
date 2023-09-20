palavra = str(input('Digite uma palavra: ')).strip().lower()
inverso = palavra[::-1]

if palavra == inverso:
    print(f'A palavra {palavra} é um palíndromo!')
else:
    print(f'A palavra {palavra} NÃO é um palíndromo!')