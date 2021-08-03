def two_sort(a):
    a = sorted(a)
    result = a[0]
    result = result.replace("", "***")
    return result[3:-3]
