def calculate_age(year_of_birth, current_year):
    if current_year - year_of_birth == 1:
        return f'You are {current_year - year_of_birth} year old.'
    elif current_year > year_of_birth:
        return f'You are {current_year - year_of_birth} years old.'
    elif year_of_birth - current_year == 1:
        return f'You will be born in {year_of_birth - current_year} year.'
    elif year_of_birth > current_year:
        return f'You will be born in {year_of_birth - current_year} years.'
    elif year_of_birth == current_year:
        return 'You were born this very year!'
