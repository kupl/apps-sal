from math import ceil
def cooking_time(needed_power, minutes, seconds, power):
    q = float(needed_power[:-1]) / float(power[:-1])
    t = minutes * 60 + seconds
    return '{} minutes {} seconds'.format(*divmod(ceil(q * t), 60))
