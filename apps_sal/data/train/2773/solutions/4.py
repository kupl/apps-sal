def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        increment = principal * interest * (1 - tax)
        principal = principal + increment
        year = year + 1
    return year
