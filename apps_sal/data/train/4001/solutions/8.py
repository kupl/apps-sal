def dot(n, m):
    return ' o '.join(-~n * '|').join(2 * '\n').join(-~m * ['---'.join(-~n * '+')])
