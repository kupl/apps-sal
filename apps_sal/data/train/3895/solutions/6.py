def xx(s):
    return s[1:] + s[0]


def shifted_diff(a, b):
    if a == b:
        return 0
    elif sorted(a) == sorted(b):
        n = 0
        for i in range(len(b)):
            n += 1
            b = xx(b)
            if b == a:
                return n
    return -1
