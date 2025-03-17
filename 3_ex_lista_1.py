# Incluir os valores 'Abril', 'Junho' e 'Outubro' na lista meses abaixo respeitando a ordenação dos meses.

meses_completos = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

meses = ['Janeiro', 'Fevereiro', 'Março', 'Maio', 'Julho', 'Agosto', 'Setembro', 'Novembro', 'Dezembro']

for index, mes in enumerate(meses):
    if mes != meses_completos[index]:
        meses.insert(index, meses_completos[index])

print(meses)
