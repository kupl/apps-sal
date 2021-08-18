def distinct_digit_year(year):
    distinctDigits = False
    while distinctDigits == False:
        year += 1
        if len(set(str(year))) == len(str(year)):
            distinctDigits = True

    return year
