limit = 300
p = [1] + [0] * limit
for i in range(1, limit + 1):
    for k, l in enumerate(range(i, limit + 1)):
        p[l] += p[k]


def exp_sum(n): return p[n]
