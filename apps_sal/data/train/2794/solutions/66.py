def calculate_age(year_of_birth, current_year):
    x = year_of_birth - current_year
    if x > 1:
        return 'You will be born in ' + str(x) + ' years.'
    if x < -1:
        return 'You are ' + str(-1 * x) + ' years old.'
    if x == 0:
        return 'You were born this very year!'
    if x == -1:
        return 'You are 1 year old.'
    if x == 1:
        return 'You will be born in 1 year.'
