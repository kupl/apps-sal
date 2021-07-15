def odd_or_even(arr):
    one = 0
    for num in arr:
        one += num
    if one % 2 == 0:
        return 'even'
    elif one % 2 != 0:
        return 'odd'
