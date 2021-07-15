from statistics import mean

DIGITS = '0123456789abcdef'

def to(n, base):
    result = []
    while n:
        n, r = divmod(n, base)
        result.append(DIGITS[r])
    return ''.join(reversed(result))

def func(l):
    n = int(mean(l))
    return [n, to(n, 2), to(n, 8), to(n, 16)]
