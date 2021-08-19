def odd_or_even(arr):
    total_sum = 0
    for i in arr:
        total_sum += i
    if total_sum % 2 == 0:
        return 'even'
    else:
        return 'odd'
