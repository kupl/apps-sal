import math


def find_ball(scales, lRange):
    if type(lRange) == int:
        lRange = range(lRange)
    if len(lRange) == 1:
        return lRange[0]

    slice = int(math.ceil(len(lRange) / 3.0))
    res = scales.get_weight(lRange[:slice], lRange[slice:slice * 2])

    if res == -1:
        return find_ball(scales, lRange[:slice])
    elif res == 1:
        return find_ball(scales, lRange[slice:slice * 2])
    else:
        return find_ball(scales, lRange[slice * 2:])
