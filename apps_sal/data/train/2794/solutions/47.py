def calculate_age(b, c):
    if b == c:
        return 'You were born this very year!'
    if c - b == 1:
        return 'You are 1 year old.'
    if c > b:
        return 'You are {} years old.'.format(c - b)
    if b - c == 1:
        return 'You will be born in 1 year.'
    if b > c:
        return 'You will be born in {} years.'.format(b - c)
