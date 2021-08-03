def pattern(n):
    l = []
    for a, b in zip(range(1, n + 2), range(n + 1)):
        res = ''.join(str(x % 10) for x in range(1, a))
        spaces = n - len(res)
        if res:
            l.append(spaces * ' ' + res + res[-2::-1] + ' ' * (spaces))
    return '\n'.join(l)
