def solomons_quest(arr):
    d_t = 0
    loc = [0, 0]
    for r in arr:
        d_t += r[0]
        if r[1] > 1:
            loc[3 % r[1]] -= r[2] * 2 ** d_t
        else:
            loc[(r[1] + 1) % 2] += r[2] * 2 ** d_t
    return loc
