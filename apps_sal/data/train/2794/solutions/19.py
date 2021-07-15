def calculate_age(year_of_birth, current_year):
    r = year_of_birth - current_year

    if r == 0: return 'You were born this very year!'
    elif abs(r) > 1: year = 'years'
    else: year = 'year'

    return  f'You will be born in {r} {year}.' if r > 0 else f'You are {abs(r)} {year} old.'
