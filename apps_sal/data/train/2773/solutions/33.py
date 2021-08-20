def calculate_years(principal, interest, tax, desired):
    if principal >= desired:
        return 0
    else:
        gain = principal * interest
        taxed = gain * tax
        new_sum = principal + gain - taxed
        return 1 + calculate_years(new_sum, interest, tax, desired)
