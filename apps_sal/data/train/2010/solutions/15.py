from pprint import pprint
import sys
# sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
dat = list(map(int, input().split()))

datl = [-1] * n
datr = [-1] * n
res = [-1] * n
for i in range(n):
    datl[i] = min(i + 1, dat[i])
    if i > 0:
        datl[i] = min(datl[i], datl[i - 1] + 1)

for i in range(n):
    datr[n - 1 - i] = min(i + 1, dat[n - 1 - i])
    if i > 0:
        datr[n - 1 - i] = min(datr[n - 1 - i], datr[n - 1 - i + 1] + 1)

for i in range(n):
    res[i] = min(datl[i], datr[i])

print(max(res))
