def x(n):
    ret = [['□' for _ in range(n)] for _ in range(n)]
    for i in range(len(ret)):
        ret[i][i] = '■';
        ret[i][-1 - i] = '■';
    return '\n'.join(''.join(row) for row in ret)
