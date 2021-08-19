def score_hand(a):
    n = sum((11 if x == 'A' else 10 if x in 'JQK' else int(x) for x in a))
    for _ in range(a.count('A')):
        if n > 21:
            n -= 10
    return n
