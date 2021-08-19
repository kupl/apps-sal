def distinct_digit_year(year):
    year += 1
    if len(set(str(year))) == len(str(year)):
        return year
    return distinct_digit_year(year)
