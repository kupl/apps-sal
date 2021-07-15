def same_col_seq(val, k, col):
    n_start = int(((1 + 8 * val)**0.5 - 1) / 2) + 1
    def f(n):
        return (1 + n) * n // 2
    def get_col(n):
        return 'red' if n % 3 == 1 else 'blue'
    return [f(n) for n in range(n_start, n_start + 62) if col==get_col(n)][:k]

