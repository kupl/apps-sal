rot = dict(['00', '11', '88', '69', '96'])


def upside_down_number(n):
    s = str(n)
    return s == ''.join((rot.get(c, '') for c in reversed(s)))


def solve(a, b):
    return sum((upside_down_number(i) for i in range(a, b)))
