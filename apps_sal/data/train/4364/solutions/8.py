def odd_or_even(arr):
    test = sum(arr[-len(arr):]) % 2
    if test == 0:
        return 'even'
    else:
        return 'odd'
