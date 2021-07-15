def calculate_age(year_of_birth, current_year):
    out = current_year - year_of_birth
    if out == 1:
        return f'You are {out} year old.'
    elif out == 0:
        return 'You were born this very year!'
    elif out > 1:
        return f'You are {out} years old.'
    elif out == -1:
        return f'You will be born in {abs(out)} year.'
    else:
        return f'You will be born in {abs(out)} years.'
