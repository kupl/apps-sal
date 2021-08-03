def odd_or_even(arr):
    res = 0
    for i in arr:
        res += i
    if res % 2 == 0:
        return 'even'
    return "odd"
