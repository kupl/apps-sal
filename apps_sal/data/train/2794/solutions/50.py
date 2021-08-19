def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    if diff > 1:
        return f'You are {diff} years old.'
    elif diff < -1:
        return f'You will be born in {-diff} years.'
    elif diff == -1:
        return f'You will be born in {-diff} year.'
    elif diff == 1:
        return f'You are {diff} year old.'
    else:
        return 'You were born this very year!'  # your code here
