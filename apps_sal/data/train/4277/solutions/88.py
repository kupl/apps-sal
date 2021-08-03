import math


def difference_in_ages(ages):
    young = math.inf
    old = -math.inf
    for age in ages:
        if (age > old):
            old = age
        if (age < young):
            young = age
    return (young, old, old - young)
