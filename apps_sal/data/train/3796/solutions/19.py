def or_arrays(arr1, arr2, d=0):
    a, b = sorted([arr1, arr2], key=len)
    a = a + (len(b) - len(a)) * [d]
    return [x | y for x, y in zip(a, b)]
