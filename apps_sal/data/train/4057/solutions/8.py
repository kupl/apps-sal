def score_hand(cards):
    k = 0

    for i, x in enumerate(cards):
        if x.isdigit():
            k += int(x)

        elif x != 'A':
            k += 10

        else:
            k += 1

    if k + 10 > 21 and 'A' in cards:
        return k
    else:
        if 'A' in cards and k + 10 <= 21:
            return k + 10

    return k
