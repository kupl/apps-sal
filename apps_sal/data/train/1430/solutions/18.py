for _ in range(int(input())):
    (n, k) = map(int, input().split())
    s = 0
    if n % 2 == 0:
        s = int(n / 2 * (k + 2))
    else:
        s = int((n - 1) / 2 * (k + 2)) + (2 * k + 1)
    print(s)
