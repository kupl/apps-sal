def odd_or_even(arr):
    a = 0
    for i in range(len(arr)):
        a += arr[i]
    if a % 2 == 0:
        return 'even'
    else:
        return 'odd'
