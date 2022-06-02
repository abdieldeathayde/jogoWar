
#for carta in cartas:
 #   print(carta)

#cartas = {'A': 14, 'K':13,  'Q':12,  'J': 11, 'T': 10}
# A = 14
# K = 13
# Q = 12
# J = 11
# T = 10
# cartas_maiores = [ 14, 13, 12, 11, 10]
# cartas_menores =[ 9, 8, 7, 6, 5, 4, 3, 2]

import random

jogador1 = 1
jogador2 = 2

pontos_jogador2 = 0
pontos_jogador1 = 0

cont_cartas_jogador1 = 2
cont_cartas_jogador2 = 2

while (cont_cartas_jogador1 > 0 and cont_cartas_jogador2 > 0):
    
    rodada_jogador = random.randint(jogador1, jogador2)
    print("Vez do jogador: ", rodada_jogador)

    carta = random.randint(2,14)
    print("Carta: ", carta)
    
    if rodada_jogador == 1:
        pontos_jogador1 = pontos_jogador1 + carta    
        print(f"Jogador {rodada_jogador} Está com: {pontos_jogador1}  Pontos")

        cont_cartas_jogador1 -= 1
    else: 
        pontos_jogador2 += carta
        print(f"Jogador {rodada_jogador} Está com: {pontos_jogador2}  Pontos")

        cont_cartas_jogador2 -= 1
        
if cont_cartas_jogador1 > cont_cartas_jogador2:
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")