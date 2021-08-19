def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if abs(age) == 1:
        unit = 'year'
    else:
        unit = 'years'
    if age == 0:
        return 'You were born this very year!'
    if age > 0:
        return 'You are ' + str(age) + ' ' + unit + ' old.'
    else:
        return 'You will be born in ' + str(abs(age)) + ' ' + unit + '.'
