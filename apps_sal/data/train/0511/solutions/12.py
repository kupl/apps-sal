from functools import reduce
from operator import xor

N, *A = map(int, open(0).read().split())
B = reduce(xor, A)
print(*map(lambda a: B ^ a, A))
