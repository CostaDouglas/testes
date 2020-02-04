from time import sleep
print('bem vindo ao elevador ')
p = int(input('quantos andares o prédio tem?: '))
a = 0
b = 1
while b != 0:

    b = int(input('\ndigite o numero do andar desejado ou digite o andar atual para consultar as informações:  '))

    if b >= 0 or b <= p:
        if b > a:
            for c in range(a, b):

                if a < b:
                    a += 1
                    print(a)
                    sleep(1)
            print(' você está no andar {}.'.format(a))


        elif b < a:
            n = a - b
            for c in range(0, n):
                a -= 1
                print(a)
                sleep(1)
            print(' você está no andar {}.'.format(a))

        elif b == a:
            dto = p-a
            print('o prédio tem {} andares.'.format(p))
            print('você está a {} andar(es) do térreo, e a {} andar(es) do topo.'.format(a, dto))
            print('você está no andar {}.'.format(a))

    else:
        print('\n erro. ')

print('acabou.')








