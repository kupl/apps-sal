def calculate_age(y, c):
    if c-y==1:
        return f'You are 1 year old.'
    if y-c==1:
        return f'You will be born in 1 year.'
    if c>y:
        return f'You are {c-y} years old.'
    if c<y:
        return f'You will be born in {y-c} years.'
    if c==y:
        return 'You were born this very year!'
