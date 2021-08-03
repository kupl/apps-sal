import math


def alex_mistakes(number_of_katas, time_limit):
    return int(math.log(1 + (time_limit - number_of_katas * 6) / 5.0, 2))
