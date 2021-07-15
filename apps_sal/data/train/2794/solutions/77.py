def calculate_age(yb, cy):
    if cy - yb == 1:
        return f'You are 1 year old.'
    if cy - yb > 1:
        return f'You are {cy-yb} years old.'
    if cy - yb == -1:
        return f'You will be born in 1 year.'
    if cy - yb < -1:
        return f'You will be born in {yb-cy} years.'
    return f'You were born this very year!'
