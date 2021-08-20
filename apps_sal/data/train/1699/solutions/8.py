def doubles(k, n):
    s = 0
    for iK in range(1, min(k + 1, 24)):
        for iN in range(2, n + 2):
            s += 1 / (iK * iN ** (2 * iK))
    return s
