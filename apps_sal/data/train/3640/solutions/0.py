def funnel_out(funnel):
    r = ''
    h = len(funnel)
    while funnel[h - 1][0] != '~':
        r += funnel[h - 1][0]
        funnel[h - 1][0] = '~'
        i = h - 1
        j = 0
        while i > 0:
            if funnel[i - 1][j] < funnel[i - 1][j + 1]:
                funnel[i][j] = funnel[i - 1][j]
                funnel[i - 1][j] = '~'
            else:
                funnel[i][j] = funnel[i - 1][j + 1]
                funnel[i - 1][j + 1] = '~'
                j += 1
            i -= 1
    print(funnel)
    return r
