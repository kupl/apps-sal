def distinct_digit_year(year):
    distinctDigits = False
    while distinctDigits == False:
        # iterate to next year until a year with distinct digits is found
        year += 1
        # if the length of the unique digits in year is the same as the total number of digits, the digits are unique
        if len(set(str(year))) == len(str(year)):
            distinctDigits = True

    return year
