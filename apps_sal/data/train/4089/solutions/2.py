def sum_dif_rev(num):
    n = 36
    while num:
        n += 9
        if n % 10 == 0:
            continue
        r = int(str(n)[::-1])
        if n != r and (n + r) % abs(n - r) == 0:
            num -= 1
    return n
