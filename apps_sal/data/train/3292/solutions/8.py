def calc(x):
    n = ''.join(map(lambda y: str(ord(y)), x))
    return n.count('7') * 6
