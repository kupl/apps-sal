def distribution_of(gold):
    gold, beggargold = gold.copy(), [0, 0]
    for pile in range(len(gold)):
        if pile % 2 == 0:
            beggargold[0] += (gold.pop(0) if gold[0] >= gold[-1] else gold.pop())
        else:
            beggargold[1] += (gold.pop(0) if gold[0] >= gold[-1] else gold.pop())
    return beggargold
