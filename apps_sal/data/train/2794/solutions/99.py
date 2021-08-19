def calculate_age(b, c):
    greet = ['You will be born in {} year{}.', 'You are {} year{} old.', 'You were born this very year!']
    return greet[2] if b == c else greet[b < c].format(abs(b - c), 's' if abs(b - c) != 1 else '')
