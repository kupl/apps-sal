def odd_or_even(arr):
    result = 0
    for number in arr:
        result = result + number
    if result % 2 == 0:
        return 'even'
    return 'odd'
