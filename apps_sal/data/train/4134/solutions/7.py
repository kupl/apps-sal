from math import ceil


def cooking_time(needed_power, minutes, seconds, power):
    totsec = minutes * 60 + seconds
    nd_pw, pw = int(needed_power.split('W')[0]), int(power.split('W')[0])
    res = ceil(nd_pw / pw * totsec)
    return '{:g} minutes {} seconds'.format(res // 60, ceil(res - (res // 60) * 60))
