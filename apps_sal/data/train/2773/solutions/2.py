def calculate_years(principal, interest, tax, desired):
    years = 0
    if principal == desired:
        return years
    while principal < desired:
        x = principal * interest
        y = x * tax
        principal = principal + x - y
        years += 1
    return years

