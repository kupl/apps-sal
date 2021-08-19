t = [n * (n + 1) // 2 for n in range(2, 32000)]
memo = {a ** 2 + b ** 2 for (a, b) in zip(t, t[1:])}


def triangular_sum(n):
    return n in memo
