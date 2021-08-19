t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + [int(i) for i in input().split()] + [0]
    l = [0] * (n + 2)
    r = [0] * (n + 2)
    for i in range(1, n + 1):
        l[i] = min(l[i - 1] + 1, a[i])
    for i in range(n, 0, -1):
        r[i] = min(r[i + 1] + 1, a[i])
    max_h = 0
    for i in range(1, n + 1):
        height = min(l[i], r[i])
        max_h = max(max_h, height)
    ans = sum(a) - max_h ** 2
    print(ans)
