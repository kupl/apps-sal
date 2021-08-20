t = int(input())
for _ in range(t):
    (n, a, b, c, d, p, q, y) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    ans = abs(l[b - 1] - l[a - 1]) * p
    x = abs(l[c - 1] - l[a - 1]) * p
    if x <= y:
        x = y + abs(l[d - 1] - l[c - 1]) * q + abs(l[b - 1] - l[d - 1]) * p
        ans = min(ans, x)
    print(ans)
