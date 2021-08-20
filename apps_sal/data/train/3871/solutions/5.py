def binary_simulation(s, r):
    ix = tuple((1 << n for n in range(len(s) + 1)))[::-1]
    tome = []
    n = int(s, 2)
    for (v, *x) in r:
        if v == 'I':
            n ^= ix[x[0] - 1] - ix[x[1]]
        else:
            tome.append(str(min(1, n & ix[x[0]])))
    return tome
