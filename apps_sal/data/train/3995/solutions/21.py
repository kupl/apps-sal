from math import floor


def dating_range(age: int) -> str:
    """ Get the minimum and maximum age range for dating. """
    return f'{floor(age / 2 + 7)}-{floor((age - 7) * 2)}' if age > 14 else f'{floor(age - 0.1 * age)}-{floor(age + 0.1 * age)}'
