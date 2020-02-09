import random
print('\n   BEM VINDO AO MUNDO RPG DE NARNIA\n\n')

player_vida = 500
player_st = 100
inimigo_vida = 50
inimigos = []


num = int(input('dijite o numero de inimigos: '))
for i in range (num):
            inimigos.append(inimigo_vida)

print('\nCada ataque dara um dano entre 10 e 15 \nCada cura custa 10 de ST curando entre 10 e 15 de HP \nO ST é recuperado em 3 a cada turno\n')

while player_vida > 0 and len(inimigos) != 0:

    print('\nhp = %i'%player_vida)
    print('ST = %i'%player_st)
    act = int(input('\nDijite 1 para ataque ou 2 para cura: '))


    if act == 1:
        d = random.randint(0, num-1)
        x = random.randint(10, 15)
        inimigos[d] -= x
        print('o inimigo %i sofreu %i de dano'%(d+1, x))

        for j in range(len(inimigos)):
            if inimigos[j-1] <= 0:

                inimigos.remove(inimigos[j-1])



        for e in range(len(inimigos)):
            o = random.randint(0,4)
            player_vida -= o
            if o > 0:
                print('inimigo %i com %i vida, deu %i de dano '%(e+1, inimigos[e], o))

            elif o == 0:
                print('inimigo %i com %i vida, errou o ataque'%(e+1, inimigos[e]))



    elif act == 2:
        player_st -= 10
        if player_vida > 474 and player_vida < 481:
            c = 500 - player_vida
            player_vida += random.randint(10, c)

        elif player_vida > 480:
            c = 500 - player_vida
            player_vida += c

        else:
            player_vida += random.randint(10, 15)

        for e in range(len(inimigos)):
            o = random.randint(0, 4)
            player_vida -= o
            if o > 0:
                print('inimigo %i com %i vida, deu %i de dano ' % (e + 1, inimigos[e], o))

            elif o == 0:
                print('inimigo %i com %i vida, errou o ataque' % (e + 1, inimigos[e]))

    if player_st < 100:
        player_st += 3



if player_vida > 0:
    print('\n   VOCE GANHOU PARABÉNS!!!!')

if player_vida == 0:
    print('\n   VOCÊ PERDEU, BOA SORTE NA PRÓXIMA')