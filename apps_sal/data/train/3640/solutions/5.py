def funnel_out(funnel):
    (break_outs, n) = ([], len(funnel))
    while len(break_outs) < n * (n + 1) / 2:
        break_outs.append(funnel[-1][0])
        (funnel[-1][0], prev) = ('~', 0)
        for i in range(len(funnel) - 1, 0, -1):
            m = min(funnel[i - 1][prev:prev + 2])
            index = funnel[i - 1].index(m)
            (funnel[i - 1][index], funnel[i][prev], prev) = ('~', m, index)
    return ''.join(break_outs)
