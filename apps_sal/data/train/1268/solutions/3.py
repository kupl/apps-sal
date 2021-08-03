while True:
    n, m, x = list(map(int, input().split()))
    if n == m == x == 0:
        break

    y = 0
    for i in range(n):
        y += ((m * i + x) // n)
    print(y)
