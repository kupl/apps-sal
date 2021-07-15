def odd_or_even(arr):
    a = 0
    for i in arr:
        a = a + i
    if a %2 == True:
        return 'odd'
    else:
        return 'even'
