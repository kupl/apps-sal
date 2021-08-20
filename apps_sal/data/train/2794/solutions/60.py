def calculate_age(year_of_birth, current_year):
    x = year_of_birth
    y = current_year
    if x < y:
        if y - x == 1:
            return 'You are 1 year old.'
        else:
            w = str(y - x)
            return 'You are ' + w + ' years old.'
    elif x == y:
        return 'You were born this very year!'
    elif x > y:
        if x - y == 1:
            return 'You will be born in 1 year.'
        else:
            k = str(x - y)
            return 'You will be born in ' + k + ' years.'
