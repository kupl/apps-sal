import math


def same_col_seq(val, k, col):
    colors = ['red', 'yellow', 'blue']
    m = colors.index(col)
    res = list()
    x0 = math.floor((-1 + math.sqrt(1 + 8 * val)) / 2)
    s = x0 * (1 + x0) // 2
    i = x0 + 1
    while len(res) < k:
        if (s + 2) % 3 == m and s > val:
            res.append(s)
        s += i
        i += 1
        if s > 3 * k * val:
            break
    return res
