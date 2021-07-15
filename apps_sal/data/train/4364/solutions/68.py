def odd_or_even(arr):
    sum_val = sum(arr)
    if sum_val % 2 == 0:
        return 'even'
    else:
        return 'odd'
