def same_col_seq(x, k, c): return (lambda n, m: [i * -~i // 2for i in range(n, n + 3 * k)if i % 3 % 2 == m][:k])(int((8 * x + 1)**.5 + 1) // 2, 'br'.find(c[0]))
