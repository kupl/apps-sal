def elements_sum(arr, d=0):
    return sum(a[i] if len(a) > i else d for i, a in enumerate(arr[::-1]))
