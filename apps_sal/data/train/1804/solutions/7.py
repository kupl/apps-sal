from itertools import cycle


def recoverSecret(ts):
    orders = set(sum([[(a, b), (b, c), (a, c)] for (a, b, c) in ts], []))
    (secret, complete) = (list(set((l for t in ts for l in t))), False)
    for (a, b) in cycle(orders):
        (i, j) = (secret.index(a), secret.index(b))
        complete = i < j and complete + 1
        if j < i:
            (secret[j], secret[i]) = (a, b)
        elif complete >= len(orders):
            break
    return ''.join(secret)
