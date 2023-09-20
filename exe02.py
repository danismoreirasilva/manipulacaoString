estado = str(input('Digite o nome de um estado: ')).strip().upper()
if estado[:3] == 'RIO':
    print(f'O estado {estado} começa com RIO!')
else:
    print(f'O estado {estado} não começa com RIO!')