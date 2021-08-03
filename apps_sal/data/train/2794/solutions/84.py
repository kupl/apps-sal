def calculate_age(year_of_birth, current_year):
    if current_year < year_of_birth:
        if current_year - year_of_birth == -1:
            return 'You will be born in 1 year.'
        else:
            return 'You will be born in ' + str(year_of_birth - current_year) + ' years.'
    elif current_year > year_of_birth:
        if current_year - year_of_birth == 1:
            return 'You are 1 year old.'
        else:
            return 'You are ' + str(current_year - year_of_birth) + ' years old.'
    else:
        return 'You were born this very year!'
