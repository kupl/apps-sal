from re import findall


def val(s):
    if not s:
        return 1
    if s[0] == '+':
        return int(s[1:] or '1')
    if s[0] == '-':
        return -int(s[1:] or '1')
    return int(s)


def differentiate(equation, point):
    res = 0
    for x in findall('[+-]?\\d*x(?:\\^\\d+)?', equation):
        i = x.find('x')
        (v, p) = (val(x[:i]), int(x[i + 2:] or '1'))
        res += v * p * point ** (p - 1)
    return res
