def distinct_digit_year(year):
    return next(i for i in range(year + 1, 9999) if len(set(str(i))) == 4)
