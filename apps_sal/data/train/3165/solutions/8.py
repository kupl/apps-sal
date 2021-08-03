# from https://oeis.org/A139250

def msb(n):
    t = 0
    while (n >> t) > 0:
        t += 1

    return 2 ** (t - 1)


def toothpick(n):
    k = (2 * msb(n) ** 2 + 1) // 3

    if n == 0:
        return 0
    elif n == msb(n):
        return k
    else:
        return k + 2 * toothpick(n - msb(n)) + toothpick(n - msb(n) + 1) - 1
