cpf = str(input('Digite o seu CPF no formato xxx.xxx.xxx-xx: ')).strip()
'''cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
print(cpf)'''

#Remove a máscara do CPF considerando que a entrada está no formato correto
cpf_somente_num = ''.join(filter(str.isdigit, cpf))
print(f'O CPF formatado, somente com números: {cpf_somente_num}')