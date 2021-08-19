def calculate_age(yob, cy):
    if yob < cy and cy - yob == 1:
        return f'You are 1 year old.'
    if yob < cy:
        return f'You are {cy - yob} years old.'
    if yob > cy and yob - cy == 1:
        return f'You will be born in 1 year.'
    if yob > cy:
        return f'You will be born in {yob - cy} years.'
    if yob == cy:
        return 'You were born this very year!'
