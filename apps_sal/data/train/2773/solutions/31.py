def calculate_years(principal, interest, tax, desired, years=0):
    if principal >= desired:
        return years
    principal += principal * interest * (1.0 - tax)
    return calculate_years(principal, interest, tax, desired, years + 1)
