print('bem vindo ao elevador ')
p = int(input('quantos andares o prédio tem?: '))
a = 0
print('\nvocê está no andar 0. ')
b = 1
while b != 0:
    b = int(input('dijite 1 para subir, 2 para descer, ou 3 para consultar as informações:  '))

    if b == 1:
        if a < p:
            a += 1
            print('\n você está no andar {}.'.format(a))
        else:
            print('\n voce ja está no ultimo andar.')

    elif b == 2:
        if a > 0:
            a -= 1
            print('\n você está no andar {}.'.format(a))
        else:
            print('\n voce ja está no térreo. ')

    elif b == 3:
        dto = p-a
        print('\n o prédio tem {} andares.'.format(p))
        print(' você está no andar {}.'.format(a))
        print(' voce esta a {} andares do térreo, e a {} do topo.'.format(a, dto))

    else:
        print('\nvoce fez merda. ')

print('acabou.')







