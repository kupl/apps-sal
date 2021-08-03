def calculate_age(year_of_birth, current_year):
    if current_year > year_of_birth:
        if current_year - year_of_birth == 1:
            return 'You are {} year old.'.format(current_year - year_of_birth)
        else:
            return 'You are {} years old.'.format(current_year - year_of_birth)
    elif current_year == year_of_birth:
        return 'You were born this very year!'
    else:
        if year_of_birth - current_year == 1:
            return 'You will be born in {} year.'.format(year_of_birth - current_year)
        else:
            return 'You will be born in {} years.'.format(year_of_birth - current_year)
