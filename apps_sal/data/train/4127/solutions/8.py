def count_pairs_int(diff, below):
    nds = [0] * below
    for i in range(1, below):
        for j in range(i, below, i):
            nds[j] += 1
    return sum(x == y for x, y in zip(nds, nds[diff:]))
