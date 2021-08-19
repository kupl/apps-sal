t = int(input())
for _ in range(t):
    (x, n) = map(int, input().strip().split())
    n -= 1
    k = n // x
    ans = k / 2 * (2 * x + (k - 1) * x)
    print(int(ans))
