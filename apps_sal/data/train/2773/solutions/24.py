def calculate_years(principal, interest, tax, desired, count=0):
    return count if principal >= desired else calculate_years(principal * (1 + interest * (1 - tax)), interest, tax, desired, count + 1)
