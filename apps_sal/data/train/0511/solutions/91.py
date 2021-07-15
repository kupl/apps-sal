n = int(input())
a = list(map(int, input().split()))
from functools import reduce
from operator import xor
xorsum = reduce(xor, a)
print(*[x^xorsum for x in a])
