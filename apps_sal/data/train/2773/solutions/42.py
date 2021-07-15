def calculate_years(principal, interest, tax, desired):
    current = principal
    years = 0
    while current < desired:
        currentstep = (current * (1 + interest))
        taxloss = (currentstep - current) * tax
        current = currentstep - taxloss
        years += 1
    return years

