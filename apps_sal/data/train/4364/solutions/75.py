def odd_or_even(arr):
    return [0] if not arr else 'odd' if sum(arr) % 2 else 'even'
