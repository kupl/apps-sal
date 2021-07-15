from functools import reduce

def cup_and_balls(b, arr):
    return reduce(lambda x, y: y[1] if x == y[0] else y[0] if x == y[1] else x, arr, b)
