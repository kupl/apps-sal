from itertools import zip_longest


def battle(player1, player2):
    rem = {'player1': [], 'player2': []}
    for (c1, c2) in zip_longest(player1, player2, fillvalue=[0, 0]):
        if c1[1] > c2[0]:
            rem['player1'].append(c1)
        if c2[1] > c1[0]:
            rem['player2'].append(c2)
    return rem
