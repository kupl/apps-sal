T = int(input())
for _ in range(T):
    A = int(input())

    total_ip = A
    total_op = 1
    total_profit = total_ip - total_op
    B = 1
    d1 = 1
    d2 = 1
    c = 1
    f = 1
    cprofit = A - B

    while total_profit >= 0:
        c = c + 1
        B = B * 2
        cprofit = A - B
        total_ip = total_ip + A
        total_op = total_op + B
        total_profit = total_ip - total_op

        if cprofit <= 0 and f != 0:
            f = 0
            d2 = c - 1
        if total_profit <= 0:
            d1 = c - 1

    print(d1, d2)
