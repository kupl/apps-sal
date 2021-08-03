def odd_or_even(arr):
    sum = 0
    for x in arr:
        sum = sum + x
    if(sum % 2 == 0):
        return 'even'
    else:
        return 'odd'
