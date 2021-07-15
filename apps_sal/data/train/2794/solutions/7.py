def calculate_age(year_of_birth, current_year):
    year = current_year - year_of_birth
    if year > 1: return f'You are {year} years old.'
    if year == 1: return f'You are {year} year old.'
    if year == -1: return f'You will be born in {abs(year)} year.'
    if year < 0: return f'You will be born in {abs(year)} years.'
    else: return 'You were born this very year!'

