def calculate_years(prin, inter, tax, desired):
    yrs = 0
    while prin < desired:
        prin = (prin * (1 + (inter * (1 - tax))))
        yrs += 1
    return yrs
