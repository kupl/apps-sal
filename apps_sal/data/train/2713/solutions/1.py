from functools import lru_cache

DIGITS = [1, 5, 10, 50]
THRESHOLD = 12

def solve_naive (n):
    minimal = n * min(DIGITS)
    maximal = n * max(DIGITS)
    return maximal - minimal

@lru_cache(maxsize=THRESHOLD)
def solve_brute (n):
    from itertools import product
    combinations = product(DIGITS, repeat=n)
    values = list(map(sum, combinations))
    return len(set(values))

@lru_cache(maxsize=THRESHOLD)
def determine_delta (tries):
    deltas = (solve_naive(n) - solve_brute(n)
              for n in range(1, tries+1))
    return max(deltas)

def solve (n):
    if n > THRESHOLD:
        return solve_naive(n) - determine_delta(THRESHOLD)
    return solve_brute(n)

