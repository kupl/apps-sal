def calculate_age(b, y):
    return (lambda d: 'You are %s year%s old.' % (d, 's' if d != 1 else '') if d > 0 else 'You will be born in %s year%s.' % (-d, 's' if d != -1 else '') if d < 0 else 'You were born this very year!')(y - b)
