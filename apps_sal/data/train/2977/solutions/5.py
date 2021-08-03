from functools import lru_cache
FC = lambda n, li=[], j=2: (FC(n, li, j + 1) if n % j else FC(n // j, li + [j], j)) if j * j <= n else sum(li + [[], [n]][n > 1])
get_factors = lru_cache(None)(lambda n: FC(n))
get_divisors = lru_cache(None)(lambda n: sum(sum([[i, n // i] for i in range(1, int(n**.5) + 1) if not n % i], [])))
def ds_multof_pfs(start, end): return [i for i in range(start, end + 1) if not get_divisors(i) % get_factors(i)]
