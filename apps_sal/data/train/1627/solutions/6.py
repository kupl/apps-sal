CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def todecimal(s, b):
    l = len(s)
    res = 0
    for i in range(l):
        c = s[i]
        val = CHARS.find(c)
        res = res + val * b**(l - i - 1)
    return res


def tobaseb(n, b):
    res = ''
    restant = n
    while restant > 0:
        res = CHARS[restant % b] + res
        restant = restant // b
    return res


def is_polydivisible(s, b):
    yes = True
    for i in range(len(s)):
        if b != 10:
            bout = str(todecimal(s[:i + 1], b))
        else:
            bout = s[:i + 1]
        if int(bout) % (i + 1) != 0:
            yes = False
            break
    return yes


def get_polydivisible(n, b):
    if n == 1:
        return '0'
    c = 0
    i = 0
    while c < n:
        if b != 10:
            ib = tobaseb(i, b)
        else:
            ib = str(i)
        if is_polydivisible(ib, b):
            c = c + 1
        i = i + 1
    return ib
