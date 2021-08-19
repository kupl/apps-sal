def pattern(n):
    inList = list([str(x) * x for x in [x for x in range(1, n + 1)]])
    return '\n'.join(inList)
