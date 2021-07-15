def sum_dif():
    yield  45
    yield  54
    yield  495
    yield  594
    n1 = 595
    while True:
        n_rev = str(n1)[::-1]
        if n_rev[0] == '0':
            n1 += 1
            continue
        n_rev_int = int(n_rev)
        if n1 - n_rev_int != 0 and (n1 + n_rev_int) % abs(n1 - n_rev_int) == 0:
            yield n1
        n1 += 1

def sum_dif_rev(n):
    p = sum_dif()
    return [next(p) for x in range(1, n+1)][-1]
