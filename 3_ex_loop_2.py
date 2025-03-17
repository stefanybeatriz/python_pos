'''
Utilizando um while loop execute um loop até que a variável contador possua valor menor que 25. 
Para cada iteração some 25 à variável soma e ao final apresente o seu resultado.'
'''

contador = 0
soma = 0

while contador < 25:
    contador += 1
    soma += 25

print(f'contador: {contador}')
print(f'soma: {soma}')
