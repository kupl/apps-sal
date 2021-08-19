b = '23456789TJQKA'


def winner(S, J):
    w1 = sum((b.index(s) > b.index(j) for (s, j) in zip(S, J)))
    w2 = sum((b.index(s) < b.index(j) for (s, j) in zip(S, J)))
    if w1 == w2:
        return 'Tie'
    if w1 > w2:
        return f'Steve wins {w1} to {w2}'
    return f'Josh wins {w2} to {w1}'
