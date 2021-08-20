import sys
from itertools import accumulate
read = sys.stdin.readline
n = int(read())
a = tuple(map(int, read().split()))
b = tuple(accumulate(map(int, read().split())))
maxs = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        t = 0
        if i != j:
            t += a[i]
            t += a[j]
            k = i
            l = j
            if i < j:
                t += b[j - 1] - b[i]
            elif i > j:
                if j > 0:
                    t += b[-1] - b[i] + b[j - 1]
                else:
                    t += b[-1] - b[i]
            else:
                pass
        else:
            t = a[i]
        if maxs < t:
            maxs = t
print(maxs)
