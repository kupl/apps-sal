def distinct_digit_year(year):
    for y in range(year + 1, 9999):
        if len(set(str(y))) == 4:
            return y
