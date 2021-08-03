import math


def cooking_time(needed_power, minutes, seconds, power):
    needed_power = int(needed_power[:-1])
    power = int(power[:-1])
    time = minutes * 60 + seconds
    res_time = math.ceil(time * needed_power / power)
    return "{0} minutes {1} seconds".format(res_time // 60, res_time % 60)
