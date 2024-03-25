# if / elif       / else
# se / se não se / se não 

entrada = input('Você quer "Entrar" ou "Sair"? ')

if entrada == 'Entrar' or entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'Sair' or entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nen entrar e nen sair')