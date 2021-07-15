def unusual_lex_order(arr):
    arr2 = []
    for elem in arr:
        arr2.append(elem[::-1])
    arr2 = sorted(arr2)
    arr3 = []
    for elem in arr2:
        arr3.append(elem[::-1])
    return arr3
