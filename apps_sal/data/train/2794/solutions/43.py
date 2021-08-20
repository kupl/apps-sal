def calculate_age(year_of_birth, current_year):
    diff = abs(year_of_birth - current_year)
    if diff == 1 and year_of_birth < current_year:
        return f'You are {current_year - year_of_birth} year old.'
    if diff != 1 and year_of_birth < current_year:
        return f'You are {current_year - year_of_birth} years old.'
    if diff == 1 and year_of_birth > current_year:
        return f'You will be born in {abs(current_year - year_of_birth)} year.'
    if year_of_birth > current_year:
        return f'You will be born in {abs(current_year - year_of_birth)} years.'
    else:
        return 'You were born this very year!'
