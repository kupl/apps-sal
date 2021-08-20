def generate_table(max_n, max_fn):
    a = []
    a.append([[0 for __ in range(_ + 1)] for _ in range(max_fn + 1)])
    for j in range(max_fn + 1):
        for k in range(j + 1):
            if j + k <= max_fn:
                a[0][j][k] = 1
    i = 1
    while 2 ** i + 1 <= max_n:
        a.append([[0 for __ in range(_ + 1)] for _ in range(max_fn + 1)])
        for j in range(max_fn + 1):
            for k in range(j + 1):
                a[i][j][k] = sum([a[i - 1][max(j, c)][min(j, c)] * a[i - 1][max(k, c)][min(k, c)] % 12345787 for c in range(max_fn + 1)])
        i += 1
    return a


def linear(s1, s2, indices, table, max_fn):
    index = indices[-1]
    if len(indices) == 1:
        return table[index][max(s1, s2)][min(s1, s2)]
    else:
        return sum([table[index][max(s1, s)][min(s1, s)] * linear(s, s2, indices[:-1], table, max_fn) for s in range(0, max_fn + 1)])


def circular_limited_sums(max_n, max_fn):
    table = generate_table(max_n + 1, max_fn)
    lengths = [2 ** i + 1 for i in range(8)]
    lengths = lengths[::-1]
    m = max_n
    indices = []
    for (index, length) in enumerate(lengths):
        while length - 1 <= m:
            indices.append(7 - index)
            m -= length - 1
    if len(indices) == 1:
        return sum([table[indices[0]][s][s] for s in range(max_fn + 1)]) % 12345787
    if len(indices) == 2:
        return sum([table[indices[0]][max(s, t)][min(s, t)] * table[indices[1]][max(s, t)][min(s, t)] for s in range(max_fn + 1) for t in range(max_fn + 1)]) % 12345787
    if len(indices) >= 3:
        return sum([table[indices[0]][max(s, s1)][min(s, s1)] * table[indices[1]][max(s, s2)][min(s, s2)] * linear(s1, s2, indices[2:], table, max_fn) for s in range(max_fn + 1) for s1 in range(max_fn + 1) for s2 in range(max_fn + 1)]) % 12345787
