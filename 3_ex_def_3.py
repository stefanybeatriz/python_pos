# Crie uma função que receba como parâmetro a string 'BaCeDiFoGu', substitua as vogais pela letra 'q' e retorne o resultado obtido.

string = 'BaCeDiFoGu'

def vogal_vira_q(string):
    vogais = 'aeiouAEIOU'
    for vogal in vogais:
        string = string.replace(vogal, 'q')

    print(string)

# Teste
vogal_vira_q(string)
