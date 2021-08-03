def pyramid(n):
    result = ''
    for x in range(n, 0, -1):
        result += '{}/{}\\\n'.format(' ' * (x - 1), ('_' if x == 1 else ' ') * ((n - x) * 2))
    return result
