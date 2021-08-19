from itertools import zip_longest


def battle(player1, player2):
    result = {'player1': [], 'player2': []}
    for ((p1, t1), (p2, t2)) in zip_longest(player1, player2, fillvalue=[0, 0]):
        if t1 > p2:
            result['player1'].append([p1, t1])
        if t2 > p1:
            result['player2'].append([p2, t2])
    return result
