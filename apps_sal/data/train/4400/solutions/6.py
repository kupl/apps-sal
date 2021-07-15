from itertools import accumulate

def minimum_steps(numbers, value):
    return next(i for i, x in enumerate(accumulate(sorted(numbers))) if x >= value)
