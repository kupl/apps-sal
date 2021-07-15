def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0: return 'You were born this very year!'
    elif age == 1: return f'You are {age} year old.'
    elif age > 1: return f'You are {age} years old.'
    elif age ==-1: return f'You will be born in {-age} year.'
    else: return f'You will be born in {-age} years.'

