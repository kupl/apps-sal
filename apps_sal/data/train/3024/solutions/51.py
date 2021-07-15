def friend(x):
    nl = []
    for f in range(len(x)):
        if len(x[f]) == 4:
            nl.append(x[f])
    return nl
