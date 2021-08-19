while 1:
    (n, m, x) = map(int, input().split())
    if n == 0 and m == 0 and (x == 0):
        break
    cost = 0
    for j in range(n):
        cost += (x + j * m) // n
    print(cost)
