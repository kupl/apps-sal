from itertools import zip_longest


def battle(player1, player2):
    res = {"player1": [], "player2": []}
    for c1, c2 in zip_longest(player1, player2, fillvalue=[0, 0]):
        if c2[0] < c1[1]:
            res["player1"].append(c1)
        if c1[0] < c2[1]:
            res["player2"].append(c2)
    return res
