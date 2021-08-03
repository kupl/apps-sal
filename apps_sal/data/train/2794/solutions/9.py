def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth
    s = 's' if abs(diff) > 1 else ''
    return f'You are {diff} year{s} old.' if diff > 0 else f'You will be born in {-diff} year{s}.' if diff < 0 else 'You were born this very year!'
