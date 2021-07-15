def calculate_years(principal, interest, tax, desired):
    years = 0
    if principal >= desired: return 0
    while True:
        yearly_interest = principal * interest
        principal = principal + yearly_interest - yearly_interest * tax
        years += 1
        if principal >= desired: break
    return years
