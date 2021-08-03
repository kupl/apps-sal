from functools import reduce
from operator import xor

N = int(input())
*A, = map(int, input().split())
Z = reduce(xor, A)
print(*[Z ^ a for a in A])
