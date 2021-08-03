for t in range(int(input())):
    n, b, m = list(map(int, input().split()))
    ans = 0
    while n > 0:
        ans += b
        half = (n + 1) / 2 if n % 2 else n / 2
        ans += m * half
        m *= 2
        n = n - half
    print(ans - b)
