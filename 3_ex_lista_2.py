'''
A lista estados abaixo, a qual uma lista que deveria conter apenas as siglas de estados brasileiros, 
contém valores inconsistentes com o seu propósito. 
Remova estes valores e ordene a lista final.'
Nota: Existe um erro de digitação em um dos estados da lista. Corrija o mesmo.
'''

estados = ['RJ', 'DF', 'PS', 44, 'PA', 9.33, 'AC', 'José', 12, 'ES']

estados.remove('PS')
estados.insert(2, 'SP')

estados.remove('José')
estados.remove(9.33)
estados.remove(12)
estados.remove(44)

print(estados)
