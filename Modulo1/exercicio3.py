"""
for in com listas
"""

lista = ['João', 'Pedro', 'Marco']
lista.append('Lucas')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))