def minimum_steps(n, v):
    k = sorted(n)[0]
    for c in range(len(n)):
        if k >= v:
            return c
        else:
            k += sorted(n)[c + 1]

