from math import log10, ceil

def solve(n):
    return max([n] + [n-n%10**x-1 for x in range(ceil(log10(n)))], key=lambda n: sum(map(int, str(n))))
