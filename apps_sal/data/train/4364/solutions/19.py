def odd_or_even(arr):
    if arr:
        return 'odd' if sum(arr) % 2 else 'even'
    else:
        return 'even'
