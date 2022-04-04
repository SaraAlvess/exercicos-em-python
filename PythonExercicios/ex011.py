lar = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = lar * h
print('Sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(lar, h, a))
t = a / 2
print('Para pintar essas parede, você precisará de {}L de tinta'.format(t))
