"""
Listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis = índices e fatiamento
métodos úteis: 
append - Adiciona um item ao final
insert - Adiciona um item no indice escolhido
 pop - Remove do final ou do índice escolhido
 del - apaga um índice
 clear - limpa a lista
 extend - estende a lista
 + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista.append('Matheus')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])