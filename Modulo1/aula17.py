# Operadores Lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira
# São considerados falsy (que vc ja viu)
# 0 0.0 '' False
# também existe o tipo none que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = int(input("Senha : "))

senha_permitida = 123456

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
elif (entrada == 'E' or entrada == 'e') and senha_digitada != senha_permitida:
    print('Senha invalida')
else:
    print('Sair')

print(True and True and True)
print(True and 0 and True)