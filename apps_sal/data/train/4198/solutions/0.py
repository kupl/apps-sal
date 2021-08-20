def simplify(n):
    for d in range(int(n ** 0.5), 0, -1):
        if not n % d ** 2:
            break
    if d * d == n:
        return '%d' % d
    elif d == 1:
        return 'sqrt %d' % n
    else:
        return '%d sqrt %d' % (d, n // d ** 2)


def desimplify(s):
    (x, _, y) = s.partition('sqrt')
    return int(x or '1') ** 2 * int(y or '1')
