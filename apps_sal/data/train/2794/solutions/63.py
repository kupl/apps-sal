def calculate_age(year_of_birth, current_year):
    y =  current_year - year_of_birth
    if y == 0:
        return 'You were born this very year!'
    else:
        s = 's' if abs(y) != 1 else ''
        if y > 0:
            return 'You are {} year{} old.'.format(y, s)
        else:
            return 'You will be born in {} year{}.'.format(abs(y), s)
        

