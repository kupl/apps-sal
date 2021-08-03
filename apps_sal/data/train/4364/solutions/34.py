def odd_or_even(arr):
    arr = sum(arr)
    return ['even', 'odd'][arr % 2]
