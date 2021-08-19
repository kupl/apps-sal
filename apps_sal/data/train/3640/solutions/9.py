def funnel_out(funnel):
    (result, funnel) = ([], funnel[::-1])

    def move(i=0, j=0):
        if i < len(funnel) - 1:
            (c1, c2) = funnel[i + 1][j:j + 2]
            if c1 and (not c2 or c1 < c2):
                funnel[i][j] = c1
                return move(i + 1, j)
            elif c2 and (not c1 or c2 < c1):
                funnel[i][j] = c2
                return move(i + 1, j + 1)
        funnel[i][j] = ''
    while funnel[0][0]:
        result.append(funnel[0][0])
        move()
    return ''.join(result)
