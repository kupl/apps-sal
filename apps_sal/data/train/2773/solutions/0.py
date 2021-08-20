def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += interest * principal * (1 - tax)
        years += 1
    return years
