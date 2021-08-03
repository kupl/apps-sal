t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    L, R = [0] * (n + 2), [0] * (n + 2)

    for i in range(1, n + 1):
        L[i] = min(L[i - 1] + 1, h[i - 1])
    for i in range(n, 0, -1):
        R[i] = min(R[i + 1] + 1, h[i - 1])

    mx = 0
    for i in range(1, n + 1):
        mx = max(mx, min(L[i], R[i]))

    ans = sum(h) - mx ** 2
    print(ans)
