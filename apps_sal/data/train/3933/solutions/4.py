def hydrate(drink_string):
    c = 0
    for i in '123456789':
        c += int(i) * drink_string.count(i)
    k = 'glass' if c == 1 else 'glasses'
    return f'{c} {k} of water'
