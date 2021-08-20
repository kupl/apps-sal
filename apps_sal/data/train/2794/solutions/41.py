def calculate_age(y, cy):
    r = cy - y
    y = 'year' + ((abs(r) > 1 or '') and 's')
    return f'You are {r} {y} old.' if r > 0 else f'You will be born in {r * -1} {y}.' if r < 0 else 'You were born this very year!'
