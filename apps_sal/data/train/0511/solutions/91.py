from operator import xor
from functools import reduce
n = int(input())
a = list(map(int, input().split()))
xorsum = reduce(xor, a)
print(*[x ^ xorsum for x in a])
