def calculate_age(year_of_birth, current_year):
    age = abs(current_year - year_of_birth)
    if current_year - year_of_birth == 1:
        return 'You are 1 year old.'
    if current_year - year_of_birth == -1:
        return 'You will be born in 1 year.'
    if current_year > year_of_birth:
        return f'You are {age} years old.'
    if current_year < year_of_birth:
        return f'You will be born in {age} years.'
    else:
        return 'You were born this very year!'
