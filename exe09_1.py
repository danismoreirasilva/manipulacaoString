data = str(input('Digite uma data no formato dd/mm/aaaa: ')).strip()
dia = data[:2]
mes = data[3:5]
ano = data[6:]
print(dia)
print(mes)
print(ano)
if int(mes) > 6:
    print(f'Mês {mes} está no segundo semestre do ano!')
else:
    print(f'Mês {mes} está no primeiro semestre do ano!')