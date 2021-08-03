def odd_or_even(arr):
    sum = 0
    for i in arr:
        sum += i
    if sum % 2 == 0:
        return 'even'
    elif sum % 2 != 0:
        return 'odd'
    elif sum == 0:
        return [0]


odd_or_even([0, 1, 2])
