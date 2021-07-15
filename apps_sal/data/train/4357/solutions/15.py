def nth_smallest(arr, pos):
    if len(arr) == 1 : return arr[0]
    big, lit, pivot = [], [], arr[pos-1]
    for i in arr:
        if   i > pivot:  big.append(i)
        elif i < pivot:  lit.append(i)
    k = len(arr) - len(big)
    if   pos > k:  return nth_smallest(big, pos - k)
    elif pos > len(lit):      return pivot
    else:                     return nth_smallest(lit, pos)
