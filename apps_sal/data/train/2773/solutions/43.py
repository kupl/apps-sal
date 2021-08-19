def calculate_years(principal, interest, tax, desired):
    import math
    count = 1
    compounding = principal * interest * (1 - tax) + principal
    if desired == principal:
        return 0
    while compounding < desired:
        compounding = compounding * interest * (1 - tax) + compounding
        count += 1
    return count
