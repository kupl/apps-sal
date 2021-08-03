l = {j: i for i, j in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')}
l_ = dict(enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))


def is_polydivisible(n, base): return next((0 for i in range(1, len(n) + 1) if get_base(n[:i], base) % i), 1)
def get_base(n, base): return sum(int(l[j]) * (base ** i) for i, j in enumerate(n[::-1]))


def get_polydivisible(n, base):
    c = i = 0
    r = ''
    while c < n:
        t = to_base(i, base)
        if is_polydivisible(t, base):
            c += 1
            r = t
        i += 1
    return ''.join(r) or '0'


def to_base(n, base):
    li = []
    while n:
        n, b = divmod(n, base)
        li.append(l_[b])
    return li[::-1]
