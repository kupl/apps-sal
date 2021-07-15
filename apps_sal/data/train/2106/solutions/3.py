#!/usr/bin/env python3

odd, even = [], []
player1_turn = True
player1 = player2 = 0
pile_number = int(input())

for _ in range(pile_number):
    n, *pile = tuple(map(int, input().split()))
    if n % 2 == 0:
        even.append(pile)
    else:
        odd.append(pile)

for pile in even:
    n = len(pile)
    player1 += sum(pile[:n//2])
    player2 += sum(pile[n//2:])

for pile in sorted(odd, reverse=True, key=lambda x: x[len(x)//2]):
    n = len(pile)
    top, middle, bottom = pile[:n//2], pile[n//2], pile[n//2+1:]
    player1 += sum(top)
    player2 += sum(bottom)
    if player1_turn:
        player1 += middle
        player1_turn = not player1_turn
    else:
        player2 += middle
        player1_turn = not player1_turn

print(player1, player2)

