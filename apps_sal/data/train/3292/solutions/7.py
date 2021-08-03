def calc(x):
    return sum(6 for c in ''.join(map(str, map(ord, x))) if c == '7')
