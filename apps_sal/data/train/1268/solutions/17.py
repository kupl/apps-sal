while True:
    n, m, x = [int(x) for x in input().split()]
    if n == m == x == 0:
        break
    ans = 0
    for i in range(1, n + 1):
        ans += (x + (i - 1) * m) // n
    print(ans)
