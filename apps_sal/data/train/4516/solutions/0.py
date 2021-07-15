def multiple(x):
    return 'Bang' * (x % 3 == 0) + 'Boom' * (x % 5 == 0) or 'Miss'
