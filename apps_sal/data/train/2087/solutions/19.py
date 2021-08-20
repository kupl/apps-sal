import sys
inf = float('inf')


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def input():
    return sys.stdin.readline().strip()


(n, l, r, ql, qr) = get_ints()
Arr = get_array()
pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] + Arr[i - 1]
ans = inf
for i in range(n + 1):
    current_cost = pre[i] * l + (pre[n] - pre[i]) * r
    if i > n - i:
        current_cost += (i - n + i - 1) * ql
    elif i < n - i:
        current_cost += (n - i - i - 1) * qr
    ans = min(ans, current_cost)
print(ans)
