def calculate_age(year_of_birth, current_year):
    y = current_year - year_of_birth
    if y > 0:
        return 'You are {} {} old.'.format(y, 'years' if y != 1 else 'year')
    elif y == 0:
        return 'You were born this very year!'
    else:
        return 'You will be born in {} {}.'.format(-y, 'years' if y != -1 else 'year')
