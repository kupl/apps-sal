def odd_or_even(arr):
    result = sum(arr)
    if result % 2 == 0:
        return 'even'
    elif result % 2 == 1:
        return 'odd'
    else:
        return [0]
