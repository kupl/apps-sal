def funnel_out(funnel):
    if not funnel:
        return ''
    ret = []
    while funnel[-1][-1]:
        j = 0
        ret.append(funnel[-1][j])
        funnel[-1][j] = None
        for i in range(-2, -len(funnel) - 1, -1):
            (_, k) = min(((funnel[i][x] or 'ÿ', x) for x in (j, j + 1)))
            (funnel[i + 1][j], funnel[i][k], j) = (funnel[i][k], funnel[i + 1][j], k)
    return ''.join(ret)
