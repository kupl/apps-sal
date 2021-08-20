def odd_or_even(arr):
    if sum(arr[:]) % 2 == 1:
        result = 'odd'
    else:
        result = 'even'
    return result
