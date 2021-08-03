import sys
input = sys.stdin.readline

n = int(input())
L, R = [], []
LR = []
INF = 10**9 + 1
m, M = INF, 0
for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    L.append(x)
    R.append(y)
    LR.append((x, y))
    if m > x:
        m = x
        idx_m = i
    if M < y:
        M = y
        idx_M = i
ans1 = (M - min(R)) * (max(L) - m)
if idx_m == idx_M:
    print(ans1)
    return
a, b = L[idx_M], R[idx_m]
if a > b:
    a, b = b, a
LR = sorted([lr for i, lr in enumerate(LR) if i != idx_m and i != idx_M])
if not LR:
    print(ans1)
    return
L, R = zip(*LR)
max_R = [-1] * (n - 2)
min_R = [-1] * (n - 2)
max_R[0] = R[0]
min_R[0] = R[0]
for i in range(n - 3):
    max_R[i + 1] = max(max_R[i], R[i + 1])
    min_R[i + 1] = min(min_R[i], R[i + 1])
l_min, l_max = L[0], L[-1]
ans2 = max(b, l_max) - min(a, l_min)
for i in range(n - 2):
    if i < n - 3:
        l_min = min(min_R[i], L[i + 1])
    else:
        l_min = min_R[i]
    l_max = max(l_max, max_R[i])
    ans2 = min(ans2, max(b, l_max) - min(a, l_min))
ans2 *= M - m
ans = min(ans1, ans2)
print(ans)
