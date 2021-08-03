from itertools import accumulate
from collections import Counter
from operator import xor
print(sum((n * (n - 1)) // 2 for n in list((Counter((i & 1, e) for i, e in enumerate(accumulate([list(map(int, input().split())) for _ in range(2)][1], xor))) + Counter([(1, 0)])).values())))
