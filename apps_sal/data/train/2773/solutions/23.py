def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        years += 1
        principal += principal * interest * (1 - tax)
    return years
