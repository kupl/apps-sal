def odd_or_even(arr):
    add = 0
    for num in arr:
        add += num
    if len(arr) == 0:
        return [0]
    if add % 2 == 0:
        return 'even'
    return 'odd'
