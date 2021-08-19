def elements_sum(arr, d=0):
    return sum((lst[i] if i < len(lst) else d for (i, lst) in enumerate(arr[::-1])))
