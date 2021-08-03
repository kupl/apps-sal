import math


def cooking_time(needed_power, minutes, seconds, power):
    t = math.ceil((60 * minutes + seconds) * int(needed_power[:-1]) / int(power[:-1]))
    return '%d minutes %d seconds' % (t // 60, t - t // 60 * 60)
