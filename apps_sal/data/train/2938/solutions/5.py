def pattern(n):

    def mkP(y):
        return str(y % 10)
    return '\n'.join([' ' * (n - x - 1) + ''.join(map(mkP, range(1, x + 1))) + ''.join(map(mkP, range(x + 1, 0, -1))) + ' ' * (n - x - 1) for x in range(n)])
