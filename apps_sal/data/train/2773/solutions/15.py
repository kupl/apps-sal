def calculate_years(sum, intr, tax, goal):
    year, fix = 0, intr * (1 - tax) + 1
    while sum < goal:
        year += 1
        sum *= fix
    return year
