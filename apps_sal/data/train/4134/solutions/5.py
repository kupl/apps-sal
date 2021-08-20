from math import ceil


def cooking_time(needed_power, minutes, seconds, power):
    total_seconds = ceil(int(needed_power[:-1]) * (minutes * 60 + seconds) / int(power[:-1]))
    (m, s) = (total_seconds // 60, total_seconds % 60)
    return '{} minutes {} seconds'.format(m, s)
