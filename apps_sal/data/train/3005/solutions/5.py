FIBS = [1, 1]

def f(n):
    # I dedicate this method to oeis.org :)
    while len(FIBS) <= n + 1:
        FIBS.append(FIBS[-2] + FIBS[-1])
    return FIBS[n + 1] - 1

