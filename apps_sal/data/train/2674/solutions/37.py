def two_sort(array):
    array.sort()
    a = array[0]
    s = ""
    for i in a:
        s = s + i + "***"
    l = len(s)
    return s[0:l - 3]
