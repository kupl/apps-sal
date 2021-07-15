from functools import reduce
from operator import xor

# via https://drken1215.hatenablog.com/entry/2020/06/22/122500

N, *A = map(int, open(0).read().split())
B = reduce(xor, A)
print(*map(lambda a: B^a, A))
