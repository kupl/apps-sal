from functools import reduce
from operator import xor
N = int(input())
A = list(map(int, input().split()))

XorA = reduce(xor, A)

B = []
for a in A:
    B.append(XorA ^ a)

print(*B)
