from itertools import accumulate
n = int(input())
a = tuple(map(int, input().split()))
b = tuple(accumulate(map(int, input().split())))
dpf = [0] * n
dpf[0] = a[0] - b[0]
for i in range(1, n):
    dpf[i] = max(dpf[i - 1], a[i] - b[i])

dpb = [0] * n
dpb[0] = a[0]
for i in range(1, n):
    dpb[i] = max(dpb[i - 1], a[i] + b[i - 1])

ans = a[0]
for i in range(1, n):
    ans = max(ans, a[i], a[i] + b[i - 1] + dpf[i - 1], a[i] + b[n - 1] - b[i] + dpb[i - 1])
print(ans)
