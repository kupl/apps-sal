def distinct(year):
    year = str(year)
    return len(year) == len(set(year))


def distinct_digit_year(year):
    year += 1
    while not distinct(year):
        year += 1
    return year
