def S2N(m, n):
    return sum(sum(i ** j for i in range(m + 1)) for j in range(n + 1))
