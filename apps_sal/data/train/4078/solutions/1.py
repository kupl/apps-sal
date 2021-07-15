def first_n_smallest(arr, n):
    m = sorted(arr)[:n]
    return [m.pop(m.index(i)) for i in arr if i in m]
