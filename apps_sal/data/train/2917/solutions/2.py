from itertools import count


def distinct_digit_year(year):
    return next((y for y in count(year + 1) if len(str(y)) == len(set(str(y)))))
