def calculate_age(year_of_birth, current_year):
    age = abs(year_of_birth - current_year)
    
    if year_of_birth < current_year:
        if age == 1:
            return 'You are {} year old.'.format(current_year - year_of_birth)
        return 'You are {} years old.'.format(current_year - year_of_birth)
    elif year_of_birth > current_year:
        if age == 1:
            return 'You will be born in {} year.'.format(year_of_birth - current_year)
        return 'You will be born in {} years.'.format(year_of_birth - current_year)
    else:
        return 'You were born this very year!'
