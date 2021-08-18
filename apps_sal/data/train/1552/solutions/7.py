
t = int(input())
for _ in range(t):
    n1, n2, m = list(map(int, input().split()))
    x = m * (m + 1)
    x /= 2
    y = min(x, min(n1, n2))
    ans = (n1 + n2) - (y + y)
    print(ans)
