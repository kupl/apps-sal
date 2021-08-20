def calculate_years(principal, interest, tax, desired):
    if principal == desired:
        return 0
    p = principal
    y = 0
    fixed = 1 + interest * (1 - tax)
    while p < desired:
        p *= fixed
        y += 1
    return y
