from collections import Counter
import math
import statistics
import itertools
a, b = list(map(int, input().split()))
lis = [input() for i in range(a)]
ra = a - 1
for i in range(ra):
    for k in range(ra - i):
        if lis[k] > lis[k + 1]:
            a = lis[k]
            lis[k] = lis[k + 1]
            lis[k + 1] = a
print(("".join(lis)))
