"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parametros (argumentos)
e retornar um vbalor específico.
Por padrão, funções Python retornam none (nada).
"""
def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(1, 2, 3)

def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Matheus')
saudacao('Ana')
saudacao('Luis')

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

"""
teste
"""
