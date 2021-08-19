from itertools import combinations as C
from functools import lru_cache as LC
get_score1 = LC(None)(lambda n: sum([sum([int(''.join(k)) for k in C(n, i)]) for i in range(1, len(n) + 1)]))
get_score2 = LC(None)(lambda n: sum((int(n[j:j + i]) for i in range(1, len(n) + 1) for j in range(len(n) - i + 1))))
get_div = LC(None)(lambda n: set(sum([[i, n // i] for i in range(2, int(n ** 0.5) + 1) if not n % i], [])))


@LC(None)
def find_int_inrange(a, b):
    d = {i: len(get_div(get_score1(str(i))) & get_div(get_score2(str(i)))) for i in range(a, b)}
    m = max(d.values())
    return [m] + [i for (i, j) in d.items() if j == m]
