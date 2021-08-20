def odd_or_even(arr):
    array = []
    for n in arr:
        total = sum(arr)
        if total % 2 == 0:
            return 'even'
        else:
            return 'odd'
