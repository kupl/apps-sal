t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    while n >= 10:
        v = n // 10 * 10
        ans += v
        n = n - v + v // 10
    print(ans + n)
