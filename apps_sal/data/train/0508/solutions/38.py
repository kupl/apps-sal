from bisect import bisect_left
import sys
input = sys.stdin.readline
(n, q) = list(map(int, input().split()))
stop = []
for i in range(n):
    (s, t, x) = list(map(int, input().split()))
    stop.append((s, t, x))
stop.sort(key=lambda x: x[2])
d = [int(input()) for i in range(q)]
R = [-1] * q
ans = [-1] * q
for (s, t, x) in stop:
    l = bisect_left(d, s - x)
    r = bisect_left(d, t - x)
    while l < r:
        if R[l] == -1:
            ans[l] = x
            R[l] = r
            l += 1
        else:
            l = R[l]
for x in ans:
    print(x)
