from itertools import accumulate

def minimum_steps(numbers, value):
    return next(i for i, s in enumerate(accumulate(sorted(numbers))) if s >= value)
