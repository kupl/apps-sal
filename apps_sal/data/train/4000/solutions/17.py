def fac(nb):
    if nb == 0:
        return 1
    res = 1
    for i in range(1, nb + 1):
        res *= i
    return res


def strong_num(number):
    nb = [int(x) for x in str(number)]
    r = 0
    for i in nb:
        r += fac(i)
    if number == r:
        return 'STRONG!!!!'
    return 'Not Strong !!'
