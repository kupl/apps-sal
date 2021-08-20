for T in range(int(input())):
    (n, m) = map(int, input().split())
    m -= 1
    x = int(m / n)
    ans = n * int(x * (x + 1) / 2)
    print(ans)
