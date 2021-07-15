from math import log

MINUTES_PER_KATA = 6.0
PUSHUPS_BASE_TIME = 5.0

def alex_mistakes(n_katas, time_limit):
    return int(log((time_limit - MINUTES_PER_KATA * n_katas) / PUSHUPS_BASE_TIME + 1, 2))
