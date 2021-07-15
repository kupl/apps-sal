def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return 'even'
    elif not sum(arr) % 2 == 0:
        return 'odd'
