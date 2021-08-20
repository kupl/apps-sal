def odd_or_even(arr):
    if len(arr) == 1 and sum(arr) == 0:
        return 'even'
    if sum(arr) % 2 == 0:
        return 'even'
    else:
        return 'odd'
