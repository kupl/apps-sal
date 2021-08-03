mod = 12345787
mat = [([1, 1], [0, 1, 3]),
       ([2, 1, -1], [0, 2, 6, 11]),
       ([2, 3, -1, -1], [0, 2, 10, 23, 70]),
       ([3, 3, -4, -1, 1], [0, 3, 15, 42, 155, 533]),
       ([3, 6, -4, -5, 1, 1], [0, 3, 21, 69, 301, 1223, 5103])]

for i in range(100):
    [m.append(sum(k * m[-1 - i] for i, k in enumerate(c)) % mod) for c, m in mat]


def circular_limited_sums(max_n, max_fn): return mat[max_fn - 1][1][max_n]
