from re import match

memo = {}


def solve(a, b):
    return sum(1 for n in range(a, b) if is_eviternity(n))


def is_eviternity(n):
    if n not in memo:
        s = str(n)
        memo[n] = match(r'[853]+$', s) and s.count('8') >= s.count('5') >= s.count('3')
    return memo[n]
