while True:
    (n, m, x) = map(int, input().split())
    if n == 0 and m == 0 and (x == 0):
        break
    money = 0
    for i in range(n):
        money = money + (x + m * i) // n
    print(money)
