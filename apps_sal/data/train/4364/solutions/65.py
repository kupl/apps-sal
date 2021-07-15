def odd_or_even(arr):
    summary = 0
    for item in range(len(arr)):
        summary = summary + arr[item]
    if summary % 2 == 0:
        return 'even'
    else:
        return 'odd'
