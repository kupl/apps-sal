from copy import deepcopy


def funnel_out(funnel):
    funnel, ans, depth = deepcopy(funnel), [], len(funnel)
    for _ in range(depth * (depth + 1) // 2):

        ans.append(funnel[-1][0])                                                # Archive current lowest char
        i, funnel[-1][0] = 0, "~"                                                # Starting position (i) / erase current char (use "~" as empty cell: higher ascii value than any letter)

        for d in range(depth - 1, 0, -1):                                          # Will swap the current char with the appropriate one from the line above
            iUp = min((i, i + 1), key=lambda x: funnel[d - 1][x])  # search the lower char index in the above level
            if funnel[d - 1][iUp] == "~":
                break  # no more chars to swap....
            funnel[d][i], funnel[d - 1][iUp] = funnel[d - 1][iUp], funnel[d][i]  # make the swap
            i = iUp  # update thte current column index

    return ''.join(ans)
