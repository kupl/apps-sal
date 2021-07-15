from itertools import count

def round_to_next5(n):
    return next(val for val in count(n) if val % 5 == 0)

