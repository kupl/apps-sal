def reg_sum_hits(dices, sides=6):
    (d, s) = (sides * [1], sides - 1)
    for i in range(dices - 1):
        t = s * [0] + d + s * [0]
        d = [sum(t[i:i + sides]) for i in range(len(t) - s)]
    return [[i + dices, prob] for (i, prob) in enumerate(d)]
