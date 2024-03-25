"""
Listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis = índices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido:', ultimo_valor)