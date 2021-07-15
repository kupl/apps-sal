def two_sort(array):
    arr = [i.split() for i in min(array)]
    return "***".join([i for j in arr for i in j])
