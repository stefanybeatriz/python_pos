# Crie uma função que receba como parâmetro a mesma lista de valores mas que retorna apenas a soma dos números ímpares da lista.

valores = [55, 92, 427, 86, 10, 64, 89, 177]

def soma_impar(valores):
    impares = []
    for valor in valores:
        if valor % 2 != 0:
            impares.append(valor)

    print(f'Os números ímpares da lista são: {impares}')
    print(f'A soma dos números ímpares de lista é {sum(impares)}')

# Teste
soma_impar(valores)
