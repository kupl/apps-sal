t = int(input())
for I in range(t):
    n = int(input())
    a = [0] + [int(i) for i in input().split()] + [0]
    L = [0] * (n + 2)
    R = [0] * (n + 2)
    for i in range(1, n + 1):
        L[i] = min(1 + L[i - 1], a[i])
    for i in range(n, 0, -1):
        R[i] = min(R[i + 1] + 1, a[i])
    max_height = 0
    for i in range(1, n + 1):
        ht = min(L[i], R[i])
        max_height = max(max_height, ht)
    ans = sum(a) - max_height ** 2
    print(ans)
