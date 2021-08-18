def row_sum_odd_numbers(n):

    k = int((1 + n) * n / 2)
    m = int((1 + n - 1) * (n - 1) / 2)

    if(k == 1):
        return 1

    x = 0
    y = 0
    z = 0
    w = 0

    for i in range(k):
        if i == 0:
            x = 1
        else:
            x = x + 2
        z = z + x

    for i in range(m):
        if i == 0:
            y = 1
        else:
            y = y + 2
        w = w + y

    return z - w
