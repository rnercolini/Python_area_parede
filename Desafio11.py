# Calcula a área de uma parede e a quantidade de tinta necessária
alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
a = alt * lar
t = a / 2
print('A dimensão da parede é {0}m x {1}m.'.format(alt, lar), end=" ")
print('A área é de {0:.2f}m² e serão necessários {1:.2f} litros de tinta.'.format(a, t))