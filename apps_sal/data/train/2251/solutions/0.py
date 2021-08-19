import sys
(n, m) = list(map(int, sys.stdin.readline().strip().split()))
L = [0 for i in range(0, n)]
H = [[] for i in range(0, n)]
for i in range(0, m):
    (x, y) = list(map(int, sys.stdin.readline().strip().split()))
    x = x - 1
    y = y - 1
    if x > y:
        (x, y) = (y, x)
    L[y] = L[y] + 1
    H[x].append(y)
ans = 0
for i in range(0, n):
    ans = ans + L[i] * len(H[i])
print(ans)
q = int(sys.stdin.readline().strip())
for i in range(0, q):
    v = int(sys.stdin.readline().strip()) - 1
    ans = ans - L[v] * len(H[v])
    L[v] = L[v] + len(H[v])
    while len(H[v]) > 0:
        w = H[v].pop()
        H[w].append(v)
        L[w] = L[w] - 1
        ans = ans + L[w] - len(H[w]) + 1
    print(ans)
