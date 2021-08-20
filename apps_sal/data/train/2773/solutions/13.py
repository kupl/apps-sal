def calculate_years(principal, interest, tax, desired):
    x = 0
    while principal < desired:
        add = principal * interest
        add = add - add * tax
        principal = principal + add
        x = x + 1
    return x
