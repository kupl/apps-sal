def funnel_out(funnel):
    ans = ""
    while funnel[-1][0] != "~":
        ans += funnel[-1][0]
        i, funnel[-1][0] = 0, "~"
        for d in range(len(funnel)-1, 0, -1):
            iUp = min((i, i+1), key=lambda x: funnel[d-1][x])
            funnel[d][i], funnel[d-1][iUp] = funnel[d-1][iUp], funnel[d][i]
            i = iUp
    return ans
