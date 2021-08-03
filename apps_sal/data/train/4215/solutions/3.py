def count_number(n, x): return sum(x % e == 0for e in range(1, n + 1)if e * n >= x)
