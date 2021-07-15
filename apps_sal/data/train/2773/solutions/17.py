def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        realint = principal * interest
        realtax = realint * tax
        principal = principal + realint - realtax
        year += 1
    return year
