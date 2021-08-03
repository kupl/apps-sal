def multiple(x):
    return ("Miss", "Bang", "Boom", "BangBoom")[(x % 3 == 0) + 2 * (x % 5 == 0)]
