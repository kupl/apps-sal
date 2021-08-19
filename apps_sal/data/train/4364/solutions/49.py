def odd_or_even(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
        i += 1
    if sum % 2 == 0:
        return 'even'
    else:
        return 'odd'
    pass
