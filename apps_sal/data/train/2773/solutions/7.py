def calculate_years(principal, interest, tax, desired):
    return 0 if principal >= desired else 1 + calculate_years(principal * (1+interest*(1-tax)), interest, tax, desired)
