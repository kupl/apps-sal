def odd_or_even(arr):
    arraytot = 0
    for e in arr:
        arraytot += e
    if arraytot % 2 == 0:
        return 'even'
    else:
        return 'odd'
