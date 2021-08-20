import math


def calculate_years(principal, interest, tax, desired):
    year = 0
    if int(principal) >= int(desired):
        return year
    while principal <= desired:
        principal = principal + principal * interest - principal * interest * tax
        year += 1
        if int(principal) >= int(desired):
            return year
