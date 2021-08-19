def div2(n):
    i = 0
    while n % 2 == 0:
        n = n / 2
        i += 1
    return (n, i)


def sharkovsky(a, b):
    (n1, rem1) = div2(a)
    (n2, rem2) = div2(b)
    if n1 == 1 and n2 == 1:
        return not rem1 < rem2
    elif n1 == 1 and n2 != 1:
        return False
    elif n1 != 1 and n2 == 1:
        return True
    elif rem1 == rem2:
        return n1 < n2
    else:
        return rem1 < rem2
