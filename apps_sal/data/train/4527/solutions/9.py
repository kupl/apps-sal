from numpy import sign
D = {x: i for (i, x) in enumerate('23456789TJQKA')}


def winner(deck_steve, deck_josh):
    res = [0, 0, 0]
    for (s, j) in zip(deck_steve, deck_josh):
        res[sign(D[s] - D[j])] += 1
    return f'Steve wins {res[1]} to {res[2]}' if res[1] > res[2] else f'Josh wins {res[2]} to {res[1]}' if res[1] < res[2] else 'Tie'
