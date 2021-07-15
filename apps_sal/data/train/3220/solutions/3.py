from collections import defaultdict
from fractions import Fraction

def divisorsum(n):
    s = 0
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            s += i
            s += n // i
    if i * i == n:
        s -= i
    return s

d = defaultdict(list)
for i in range(1, 2000+1):
    d[Fraction(divisorsum(i), i)].append(i)

xs = [value for key, value in d.items() if len(value) > 1]

def solve(a,b):
    ys = [[y for y in x if a <= y < b] for x in xs]
    return sum(y[0] for y in ys if len(y) > 1)
