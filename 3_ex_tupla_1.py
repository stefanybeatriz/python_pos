# Imprima todos os valores da tupla abaixo de maneira sequencial.

tupla = (6, 77, 42, 10)

# Comando para ordenar em ordem crescente e armazenagem da lista gerada na variável 'sequencia'
sequencia = sorted(tupla)
print(f'LISTA com valores ordenados: \n {sequencia}')

# Convertendo a LISTA 'sequencia' em TUPLA na variável 'tupla_sequenciada'
tupla_sequenciada = tuple(sequencia)

# Imprimindo o resultado final:
print(f'Tupla ordenada: \n {tupla_sequenciada}')
