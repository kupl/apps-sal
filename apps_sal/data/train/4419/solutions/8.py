from itertools import product


def reg_sum_hits(n, s):
    pairs = [[i, 0] for i in range(n, n * s + 1)]

    for i in product(range(1, s + 1), repeat=n):
        sum = 0
        for j in i:
            sum += j
        index = sum - n
        pairs[index][1] += 1

    return pairs
