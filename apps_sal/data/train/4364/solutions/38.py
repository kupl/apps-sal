import functools
def odd_or_even(arr):
    return 'even' if functools.reduce(lambda x, y: x + y, arr) % 2 == 0 else 'odd'
