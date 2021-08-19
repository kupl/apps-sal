while True:
    (n, m, x) = list(map(int, input().split()))
    if n == m == x == 0:
        break
    cost = 0
    for i in range(n):
        cost += (m * i + x) // n
    print(cost)
