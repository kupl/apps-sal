def f(n): return n > 1 and all(n % d for d in range(2, int(n**.5) + 1))
def goldbach_partitions(n): return []if n % 2else['%d+%d' % (p, n - p)for p in range(n // 2 + 1)if f(p) * f(n - p)]
