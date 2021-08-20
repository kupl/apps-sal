from math import log


def thue_morse(n, s='0'):
    for _ in range(int(log(n, 2)) + 1):
        s += s.translate(str.maketrans('01', '10'))
    return s[:n]
