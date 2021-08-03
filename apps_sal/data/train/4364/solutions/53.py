def odd_or_even(arr):
    if len(arr) == 0:
        arr = 0
    som = sum(arr)
    if som % 2 == 0:
        return "even"
    else:
        return "odd"
