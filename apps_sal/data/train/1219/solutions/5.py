p = int(1000000000.0 + 7)
for _ in range(int(input())):
    (n, m) = map(int, input().split())
    if n % 2 != 0:
        n = (n - 1) // 2
    else:
        n = n // 2
    b = n * (n + 1)
    ans = pow(m, b, p)
    print(ans)
