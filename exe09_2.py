data = str(input("Digite uma data no formato dd/mm/aaaa: ")).strip()
dia, mes, ano = data.split('/')
print(dia,mes,ano)

# Converte o dia, mês e ano em inteiros
dia = int(dia)
mes = int(mes)
ano = int(ano)

if mes >= 7:
    semestre = "2º"
else:
    semestre = "1º"

print(f'O dia é: {dia}')
print(f'O mês é: {mes}')
print(f'O ano é: {ano}')
print(f'A data está no {semestre} semestre.')