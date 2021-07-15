from math import floor
def dating_range(age):
    if age <= 14:
        min = floor(age - 0.1 * age)
        max = floor(age + 0.1 * age)
    else:
        min = floor(age / 2 + 7)
        max = floor((age - 7) * 2)
    return '{0}-{1}'.format(min, max)
