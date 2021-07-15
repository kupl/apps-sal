def odd_or_even(arr):
    result = 0
    for item in arr:
        result += item
    if result % 2 == 0:
        return "even"
    else:
        return "odd"
