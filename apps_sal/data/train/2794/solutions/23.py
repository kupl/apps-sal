def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    if diff == 0:
        return 'You were born this very year!'
    elif diff == 1:
        return 'You are {} year old.'.format(diff)
    elif diff > 1:
        return 'You are {} years old.'.format(diff)
    elif diff == -1:
        return 'You will be born in {} year.'.format(abs(diff))
    elif diff < -1:
        return 'You will be born in {} years.'.format(abs(diff))
