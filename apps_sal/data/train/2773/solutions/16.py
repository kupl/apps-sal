def calculate_years(principal, interest, tax, desired):
    if desired == principal:
        return 0
    else:
        years = 0
        while principal < desired:
            principal += principal * interest - principal * interest * tax
            years += 1
        return years
