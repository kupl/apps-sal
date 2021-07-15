def calculate_years(principal, interest, tax, desired):
    years = 0
    if principal == desired:
        return years
    else:
        while principal < desired:
            years += 1
            principal = principal + (principal * interest) * (1 - tax)
        return years
