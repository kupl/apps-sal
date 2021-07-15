def calculate_years(principal, interest, tax, desired):
    y = 0
    while desired > principal:
        y += 1
        principal = principal*(1+interest)-principal*interest*tax
    return y
