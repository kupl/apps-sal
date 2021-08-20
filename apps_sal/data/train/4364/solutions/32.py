def odd_or_even(arr):
    sum = 0
    for i in arr:
        sum += i
    if abs(sum) % 2 == 0:
        return 'even'
    else:
        return 'odd'
