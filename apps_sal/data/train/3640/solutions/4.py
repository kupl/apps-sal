from copy import deepcopy


def funnel_out(funnel):
    (funnel, ans, depth) = (deepcopy(funnel), [], len(funnel))
    for _ in range(depth * (depth + 1) // 2):
        ans.append(funnel[-1][0])
        (i, funnel[-1][0]) = (0, '~')
        for d in range(depth - 1, 0, -1):
            iUp = min((i, i + 1), key=lambda x: funnel[d - 1][x])
            if funnel[d - 1][iUp] == '~':
                break
            (funnel[d][i], funnel[d - 1][iUp]) = (funnel[d - 1][iUp], funnel[d][i])
            i = iUp
    return ''.join(ans)
