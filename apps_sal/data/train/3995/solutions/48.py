from math import floor
def dating_range(age):
    min_age = floor(age * .5 + 7 if age > 14 else age * .9)
    max_age = floor(age * 2 - 14 if age > 14 else age * 1.1)
    return "{}-{}".format(min_age, max_age)
