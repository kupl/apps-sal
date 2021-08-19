def f(n, m):

    def sum_1_to_n(n):
        return (n + 1) * n // 2
    (a, b) = divmod(n, m)
    return a * sum_1_to_n(m - 1) + sum_1_to_n(b)
