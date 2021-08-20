def calculate_age(year_of_birth, current_year):
    old = current_year - year_of_birth
    if old > 0:
        return 'You are {} year{} old.'.format(old, 's' if old > 1 else '')
    elif old < 0:
        return 'You will be born in {} year{}.'.format(abs(old), 's' if abs(old) > 1 else '')
    else:
        return 'You were born this very year!'
