t = int(input())
for _ in range(t):
    a = int(input())
    d1 = 0
    profit = 0
    i = 0
    while a - 2 ** i > 0:
        profit += a - 2 ** i
        i += 1
        d1 += 1
    d2 = d1
    while profit > 0:
        profit += a - 2 ** i
        i += 1
        d2 += 1
    print(d2 - 1, d1)
