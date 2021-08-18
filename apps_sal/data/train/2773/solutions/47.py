import math


def calculate_years(principal, interest, tax, desired):
    effInt = interest * (1 - tax)
    timeFloat = math.log(desired / principal) / math.log(1 + effInt)
    if desired > principal:
        return int(timeFloat) + 1
    else:
        return 0
