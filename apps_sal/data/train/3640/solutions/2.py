def pull_letter(funnel):
    letter = funnel[0][0]
    funnel[0][0] = None
    pos = 0

    for idx, level in enumerate(funnel[:-1]):
        current_pos = pos

        c1 = funnel[idx + 1][pos]
        c2 = funnel[idx + 1][pos + 1]
        if c1 is None or (c2 is not None and c1 >= c2):
            pos += 1

        level[current_pos] = funnel[idx + 1][pos]
        funnel[idx + 1][pos] = None

    return letter


def funnel_out(funnel):
    funnel = list(reversed(funnel))
    result = ''

    while funnel[0][0]:
        result += pull_letter(funnel)

    return result
