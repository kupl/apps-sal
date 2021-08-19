def sum_dif_rev(n):
    k = 0
    i = 1
    while i <= n:
        k += 1
        if str(k)[-1] != '0':
            p = int(str(k)[::-1])
            if abs(p - k) != 0:
                if (p + k) % abs(p - k) == 0:
                    i += 1
    return k
