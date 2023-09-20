email = str(input('Digite o seu e-mail: ')).strip().lower()
usuario = email[:email.find('@')]
dominio = email[email.find('@'):]
print(f'O usuário é {usuario}')
print(f'O domínio é {dominio}')