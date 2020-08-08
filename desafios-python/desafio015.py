dias = int(input('Quantidade de dias alugado: '))
km = float(input('Km percorridos: '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é {}'.format(total))
