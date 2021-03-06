from collections import deque
import sys
input = sys.stdin.readline
(inp, ip) = (lambda: int(input()), lambda: [int(w) for w in input().split()])


def getmax(x, n, k):
    mx = []
    dq = deque()
    for i in range(k):
        while dq and x[i] >= x[dq[-1]]:
            dq.pop()
        dq.append(i)
    mx.append(x[dq[0]])
    for i in range(k, n):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and x[i] >= x[dq[-1]]:
            dq.pop()
        dq.append(i)
        mx.append(x[dq[0]])
    return mx


n = inp()
m = n + n
A = ip()
B = ip()
A += A
B += B
pre = [0] * (m + 1)
for i in range(1, m + 1):
    pre[i] += pre[i - 1] + B[i - 1]
plus = [0] * m
minus = [0] * m
for i in range(m):
    plus[i] = A[i] + pre[i]
    minus[i] = A[i] - pre[i + 1]
a = getmax(plus, m, n - 1)
ans = float('-inf')
for i in range(n):
    ans = max(ans, minus[i] + a[i + 1])
print(max(ans, *A))
