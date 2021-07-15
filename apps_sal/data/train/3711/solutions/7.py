def xMasTree(n):
    width = 2*n - 1
    row = 1
    res = []
    while row <= n:
        line = ''
        buff = '_'*(n-row)
        line += buff
        line += '#'*(2*row-1)
        line += buff
        res.append(line)
        row += 1
    for x in range(2):
        line = ''
        buff = '_'*(n-1)
        line += buff
        line += '#'
        line += buff
        res.append(line)
    return res
