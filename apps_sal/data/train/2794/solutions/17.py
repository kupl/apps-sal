def calculate_age(b, c):
    return 'You are {} {} old.'.format(c - b, 'years' if c - b > 1 else 'year') if c > b else 'You will be born in {} {}.'.format(b - c, 'years' if b - c > 1 else 'year') if b > c else 'You were born this very year!'
