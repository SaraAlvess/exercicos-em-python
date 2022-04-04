d = int(input('Quantos dias usados? '))
km = float(input('Quantos kilometros rodados? '))
cd = d * 60
ckm = km * 0.15
total = cd + ckm
print('Você pagará R${:.2f} pelo aluguel do carro.'.format(total))

