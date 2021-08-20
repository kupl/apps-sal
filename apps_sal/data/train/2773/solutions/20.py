def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        year = year + 1
        interest_beforetax = interest * principal
        principal = principal + (1 - tax) * interest_beforetax
    return year
