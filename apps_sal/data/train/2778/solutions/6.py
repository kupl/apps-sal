def faro(xs):
    m = len(xs) // 2
    return [x for xs in zip(xs[:m], xs[m:]) for x in xs]

def faro_cycles(deck_size):
    xs = original = list(range(deck_size))
    n = 0
    while True:
        n += 1
        xs = faro(xs)
        if xs == original:
            return n
