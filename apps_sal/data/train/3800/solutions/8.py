import re


def to_display(b, n):
    r = []
    while n:
        (n, x) = divmod(n - 1, 26)
        r.append(chr(65 + x))
    return ''.join(r[::-1]) + str(b)


def to_internal(s):
    ((a, b), n) = (re.findall('[A-Z]+|\\d+', s), 0)
    for x in a:
        n *= 26
        n += ord(x) - 64
    return (int(b), n)


def spreadsheet(s):
    a = re.findall('[A-Z]+|\\d+', s)
    return 'R{}C{}'.format(*to_internal(s)) if len(a) == 2 else to_display(int(a[1]), int(a[3]))
