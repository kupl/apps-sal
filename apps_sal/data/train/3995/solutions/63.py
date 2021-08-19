import math


def dating_range(age):
    return '{}-{}'.format(math.floor(age - 0.1 * age), math.floor(age + 0.1 * age)) if age < 14 else '{}-{}'.format(math.floor(age / 2 + 7), math.floor((age - 7) * 2))
