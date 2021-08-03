def calculate_years(principal, interest, tax, desired):
    years = 0

    while principal < desired:
        a = principal * interest
        principal += a - (a * tax)
        years += 1

    return years
