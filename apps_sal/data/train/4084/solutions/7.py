import math


def alex_mistakes(number_of_katas, time_limit):
    return int(math.log((time_limit - number_of_katas * 6.0) / 5 + 1, 2))
