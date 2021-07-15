sum_mul = lambda n, m: 'INVALID' if n <= 0 or m <= 0 else sum(x for x in range(m) if x % n == 0)
