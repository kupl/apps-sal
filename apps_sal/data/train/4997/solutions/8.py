def f_d(m):
    return sum(set(sum([[i, m // i] for i in range(1, int(m ** 0.5) + 1) if m % i == 0], [])))


def equal_sigma1(n):
    return sum(set(sum([[i, int(str(i)[::-1]) if int(str(i)[::-1]) <= n else 0] for i in range(2, n + 1) if str(i) != str(i)[::-1] and f_d(i) == f_d(int(str(i)[::-1])) > 0], [])))
