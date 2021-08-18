def chameleon(chameleons, desiredColor):
    print(chameleons, desiredColor)
    other_coler = [j for i, j in enumerate(chameleons) if i != desiredColor]

    if sum([i == 0 for i in chameleons]) == 2 and chameleons[desiredColor] == 0:
        return -1
    elif not (other_coler[0] - other_coler[1]) % 3 == 0:
        return -1

    return max(other_coler)
