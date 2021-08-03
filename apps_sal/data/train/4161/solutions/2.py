seq = {0: 1, 1: 1}


def fusc(n):
    if n in list(seq.keys()):
        return seq[n]
    elif n % 2 == 0:
        r = fusc(n >> 1)
        seq[n] = r
        return r
    return fusc((n - 1) >> 1) + fusc((n + 1) >> 1)


def rat_at(n):
    return fusc(n + 1), fusc(n + 2)


def index_of(p, q):
    bits = ''
    while p > 1 or q > 1:
        if p > q:
            bits = "1" + bits
            p = p - q
        else:
            bits = "0" + bits
            q = q - p
    bits = "1" + bits
    return int(bits, 2) - 1
