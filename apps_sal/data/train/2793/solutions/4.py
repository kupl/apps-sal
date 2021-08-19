def group_size(S, D):

    def a000217(n):
        return (n + 1) * n // 2

    def a002024(n):
        return int((1 + (1 + 8 * n) ** 0.5) / 2)
    return a002024(D - 1 + a000217(S - 1))
