def distribution_of(piles):
    (i, gold) = (False, [0, 0])
    while piles:
        (gold[i], piles) = (gold[i] + piles[-1], piles[:-1]) if piles[-1] > piles[0] else (gold[i] + piles[0], piles[1:])
        i = not i
    return gold
