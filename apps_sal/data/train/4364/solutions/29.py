def odd_or_even(arr):
    i = 0
    for x in arr:
        i += x
    if i % 2 == 0:
        return f"{'even'}"
    else:
        return f"{'odd'}"
