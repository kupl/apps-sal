def odd_or_even(arr):
    y = int()
    for x in range(0, len(arr)):
        y += arr[x]
    if y % 2 == 0:
        return 'even'
    else:
        return 'odd'
