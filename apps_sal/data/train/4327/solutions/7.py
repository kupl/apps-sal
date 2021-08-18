def chameleon(chameleons, desiredColor):
    perm_count = 0
    if desiredColor == 0:
        cD, cA, cB = chameleons
    elif desiredColor == 1:
        cA, cD, cB = chameleons
    else:
        cA, cB, cD = chameleons

    while cA != 0 or cB != 0:
        if cA != 0 and cB != 0:
            d = min(cA, cB)
            cA, cB, cD = cA - d, cB - d, cD + 2 * d
        elif cA == 0:
            d = min(cB // 3, cD)
            cA, cB, cD = cA + 2 * d, cB - d, cD - d
        elif cB == 0:
            d = min(cA // 3, cD)
            cA, cB, cD = cA - d, cB + 2 * d, cD - d
        if d == 0:
            return -1
        perm_count += d
    return perm_count
