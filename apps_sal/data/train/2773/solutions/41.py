def calculate_years(principal, interest, tax, desired):
    year_counter = 0
    while principal < desired:
        year_counter += 1
        principal += principal * interest * (1 - tax)
    return year_counter
