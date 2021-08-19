def draw(a):
    n = iter(a)
    li = [('■' * next(n)).ljust(max(a), '□') for i in range(len(a))]
    return '\n'.join([''.join(i) for i in list(zip(*li))[::-1]])
