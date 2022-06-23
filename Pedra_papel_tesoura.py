import random

def jogar():
    usuario = input("Escolha entre pedra, papel ou tesoura? ")
    computador = random.choice(['pedra', 'papel', 'tesoura'])

    print(f'O computador escolheu {computador}')
    if usuario == computador:
        return 'Empatou!!!'

    # pe > te, te > pa, pa > pe
    if ganhou (usuario, computador):
        return 'Você ganhou!!!'

    return 'Você perdeu!!!'

def ganhou(jogador, oponente):
        if (jogador == 'pedra' and oponente == 'tesoura') or (jogador == 'tesoura' and oponente == 'papel') or \
        (jogador == 'papel' and oponente == 'pedra'):
            return True

print(jogar())