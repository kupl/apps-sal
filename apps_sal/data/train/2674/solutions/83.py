def two_sort(array):
    s = ""
    for i in (sorted(array)[0]):
        s += i + "***"

    return s[:-3]
