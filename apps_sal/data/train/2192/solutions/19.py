import sys
import bisect
n = int(input())
a, b = [], []
for _ in range(n):
    ai, bi = list(map(int, input().split(' ')))
    a.append(ai)
    b.append(bi)

dptable = [1 for i in range(n + 1)]
dptable[0] = 0
a.insert(0, -1 * sys.maxsize)
b.insert(0, 0)
ab = list(zip(a, b))
sorted(ab)
b = [x for _, x in sorted(zip(a, b))]
a.sort()
# print(a,"\n",b)
for i in range(1, len(dptable)):
    delupto = a[i] - b[i]
    delupto = bisect.bisect_left(a, delupto)
    # print(delupto,i)
    dptable[i] = dptable[delupto - 1] + 1
print(n - max(dptable))
