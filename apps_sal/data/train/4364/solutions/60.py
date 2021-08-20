def odd_or_even(arr):
    val = 0
    for i in range(len(arr)):
        val += arr[i]
    if val % 2 == 0:
        return 'even'
    else:
        return 'odd'
