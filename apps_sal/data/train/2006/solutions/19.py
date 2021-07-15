from math import gcd
from functools import reduce
n, a = int(input()), list(map(int, input().split()))
g = reduce(lambda x, y: gcd(x, y), a, 0)
print("Alice" if (max(a) // g - n) % 2 == 1 else "Bob")
