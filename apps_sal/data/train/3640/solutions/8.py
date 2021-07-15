def funnel_out(funnel):
    ans = ""
    while funnel:
        ans += funnel[-1].pop()
        funnel[-1].append('µ')
        for row in range(len(funnel) - 1, 0, -1):
            for col in range(len(funnel[row])):
                if funnel[row][col] == 'µ':
                    if funnel[row - 1][col] < funnel[row - 1][col + 1]:
                        funnel[row][col] = funnel[row - 1][col]
                        funnel[row - 1][col] = 'µ'
                    else:
                        funnel[row][col] = funnel[row - 1][col + 1]
                        funnel[row - 1][col + 1] = 'µ'
            if all(en == 'µ' for en in funnel[row]):
                del(funnel[row])
        if len(funnel) == 1:
            break
    return ans
