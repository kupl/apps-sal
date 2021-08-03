from itertools import cycle


def swap(s, n):
    return (lambda N: ''.join(e if not e.isalpha() else (e, e.swapcase())[next(N)] for e in s))(cycle(map(int, bin(n)[2:])))
