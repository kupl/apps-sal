import math


def stats_disc_distr(disv):
    m = 0
    v = 0
    p = 0
    ni = False
    for dis in disv:
        if type(dis[0]) != int:
            ni = True
        p = p + dis[1]
        m = m + dis[0] * dis[1]
    if ni == False:
        for dis in disv:
            v += (dis[0] - m) * (dis[0] - m) * dis[1]
    if ni:
        return "It's not a valid distribution and furthermore, one or more variable value are not integers" if math.fabs(p - 1) > 1e-10 else 'All the variable values should be integers'
    if math.fabs(p - 1) > 1e-10:
        return "It's not a valid distribution"
    return [m, v, v ** 0.5]
