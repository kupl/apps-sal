def calculate_age(year_of_birth, current_year):
    x = year_of_birth
    y = current_year
    if x < y and y - x == 1:
        return 'You are' + ' ' + str(y - x) + ' ' + 'year old.'
    elif x < y:
        return 'You are' + ' ' + str(y - x) + ' ' + 'years old.'
    elif x > y and x - y == 1:
        return 'You will be born in' + ' ' + str(x - y) + ' ' + 'year.'
    elif x > y:
        return 'You will be born in' + ' ' + str(x - y) + ' ' + 'years.'
    else:
        return 'You were born this very year!'
