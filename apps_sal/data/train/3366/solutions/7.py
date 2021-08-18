def sil(a):
    b = 1
    for i in range(1, a + 1):
        b = b * i
    return b


def nth_perm(n, d):
    lit = list(('0123456789')[:d])
    out = []
    for i in range(d):
        el = int((n - 1) / sil(d - 1))
        out.append(lit.pop(el))
        n = n - sil(d - 1) * (el)
        d -= 1

    return ''.join(out)
