def odd_or_even(arr):
    counter = 0
    for i in arr:
        counter += int(i)
    if counter % 2 == 0:
        return 'even'
    else:
        return 'odd'
