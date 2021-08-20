def odd_or_even(arr):
    sum = 0
    for x in arr:
        sum += x
    return 'even' * int(1 - sum % 2) + 'odd' * (sum % 2)
