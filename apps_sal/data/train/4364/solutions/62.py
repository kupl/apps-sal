def odd_or_even(arr):
    if not arr:
        arr = [0]
    return 'odd' if sum(arr) % 2 else 'even'
