def multiple(x):
    return ['Miss', 'Bang', 'Boom', 'BangBoom'][(x % 3 == 0) + (x % 5 == 0) * 2]
