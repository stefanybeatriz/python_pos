# Tente identificar o erro no bloco de código abaixo.

# ERRO: ausência dos dois pontos na condicional
nome = 'Joaquim'

if nome == 'Joaquim' # <<< localização onde deveriam estar os :
    print('O nome é Joaquim.')
else:
    print('Outro nome.')

# Código correto:
nome = 'Joaquim'

if nome == 'Joaquim':
    print('O nome é Joaquim.')
else:
    print('Outro nome.')
