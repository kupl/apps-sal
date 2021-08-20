import sys
from bisect import bisect_left as bl
input = sys.stdin.readline
(N, T) = map(int, input().split())
a = list(map(int, input().split()))
cm = [float('inf')] * (N + 1)
cmx = [0] * (N + 1)
for i in range(N):
    cm[i + 1] = min(cm[i], a[i])
    cmx[N - 1 - i] = max(cmx[N - i], a[N - 1 - i])
res = 0
x = 0
for i in range(N + 1):
    x = max(cmx[i] - cm[i], x)
for i in range(N):
    if cmx[i] - a[i] == x:
        res += 1
print(res)
