def isPP(n):
    k = 2
    m = n**(1 / k)
    while m % 1 != 0 and m > 2:
        k += 1
        m = n**(1 / k)
        m = float("{:.5f}".format(m))
    if m % 1 == 0:
        return [int(m), k]
    else:
        return None
