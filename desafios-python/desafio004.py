dado = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(dado))
print('É número?', dado.isnumeric())
print('É alfa numérico?', dado.isalnum())
print('É alfabético?', dado.isalpha())
print('Caixa baixa?', dado.islower())
print('Caixa alta?', dado.isupper())
print('É um número decimal?', dado.isdecimal())
print('É um espaço?', dado.isspace())
