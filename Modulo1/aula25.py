"""
Flag (Bandeira) - marcar um local
none = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

condicao = True
passou_no_if = None

if condicao :
   passou_no_if: True
   print('Faca algo')
else:
  print('Não faca algo')


if passou_no_if is None:
   print('Não passou no if')
else:
   print('Passou no if')