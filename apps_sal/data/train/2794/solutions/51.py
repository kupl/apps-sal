def calculate_age(year_of_birth, current_year):
    a = current_year - year_of_birth
    if a > 1:
        return f'You are {a} years old.'
    elif a == 0:
        return 'You were born this very year!'
    elif a == 1:
        return f'You are {a} year old.'
    elif a == -1:
        return f'You will be born in {abs(a)} year.'
    else:
        return f'You will be born in {abs(a)} years.'
