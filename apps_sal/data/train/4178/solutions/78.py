def min_sum(a):
    q = sorted(a)
    return sum(q[i] * q[-i - 1] for i in range(len(q) // 2))
