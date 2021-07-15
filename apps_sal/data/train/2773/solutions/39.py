def calculate_years(principal, interest, tax, desired):
    years_required = 0
    current = principal
    while (current<desired):
        current+=current*interest*(1-tax)
        years_required+=1
    return years_required

