def sum_array(a):
    try:
        a.sort()
        a = sum(a[1:-1])
    except AttributeError:
        a = 0
    return a
