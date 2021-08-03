def array_info(x):
    if not x:
        return 'Nothing in the array!'
    L = [0] * 4
    for e in x:
        if type(e) == int:
            L[0] += 1
        elif type(e) == float:
            L[1] += 1
        elif e == ' ':
            L[3] += 1
        else:
            L[2] += 1
    return [[len(x)]] + [[e or None] for e in L]
