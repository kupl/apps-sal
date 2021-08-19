def calculate_age(b, c):
    if c - b > 1:
        return 'You are {} years old.'.format(c - b)
    elif c - b == 1:
        return 'You are 1 year old.'
    elif c == b:
        return 'You were born this very year!'
    elif b - c > 1:
        return 'You will be born in {} years.'.format(b - c)
    else:
        return 'You will be born in 1 year.'
