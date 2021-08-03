def distribution_of(golds):
    ind, beggars = [0, len(golds) - 1], [0, 0]
    for n in range(len(golds)):
        i = golds[ind[0]] < golds[ind[1]]
        beggars[n % 2] += golds[ind[i]]
        ind[i] += (-1)**i
    return beggars
