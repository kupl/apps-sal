def calculate_years(principal, interest, tax, desired):
    years = 0
    gain = 0
    taxed = 0
    while principal < desired:
        years = years + 1
        gain = principal * interest
        taxed = gain * tax
        principal = principal + gain - taxed

    return years
    raise NotImplementedError("TODO: calculate_years")
