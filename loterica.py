from random import randint
i = 0
gab = []
while i < 6:
	i += 1
	num = randint(1,60)
	gab.append(num)
j = 0
ap = []
k = 0
cont = 0
while j < 6:
	j += 1
	cont +=1
	ap.append(int(input('Digite sua aposta: ')))
print('Gabarito:{}'.format(gab))
print('Aposta:{}'.format(ap))

sair = input('Aperte qualquer tecla para sair.')
