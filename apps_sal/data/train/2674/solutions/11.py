def two_sort(array):
    x = ""
    a = sorted(array)
    for alp in a[0]:
        x = x + alp + "***"
    return x[:-3]
