def calculate_age(a, b):
    if abs(a - b) > 1:
        if b > a:
            return 'You are ' + str(b - a) + ' years old.'
        elif b < a:
            return 'You will be born in ' + str(a - b) + ' years.'
    elif a - b == 0:
        return 'You were born this very year!'
    elif b - a == 1:
        return 'You are 1 year old.'
    elif a - b == 1:
        return 'You will be born in 1 year.'
