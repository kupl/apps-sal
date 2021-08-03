def calculate_age(year_of_birth, current_year):
    d = current_year - year_of_birth
    if d > 0:
        if d == 1:
            return 'You are ' + str(d) + ' year old.'
        else:
            return 'You are ' + str(d) + ' years old.'
    elif d < 0:
        if d == -1:
            return 'You will be born in ' + str(-d) + ' year.'
        else:
            return 'You will be born in ' + str(-d) + ' years.'
    else:
        return 'You were born this very year!'
