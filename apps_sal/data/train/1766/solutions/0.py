def b(n):
    if not n: return '0'
    r = []
    while n:
        r.append(n % 2)
        n = (n - n % 2) / -2
    return ''.join(str(c) for c in r[::-1])

def d(n):
    r = 0
    for c in n: r = -2 * r + int(c)
    return r

def skrzat(base, n):
    if base == 'b': return 'From binary: %s is %d' % (n, d(n))
    if base == 'd': return 'From decimal: %d is %s' % (n, b(n))
    raise ValueError('unknown base')
