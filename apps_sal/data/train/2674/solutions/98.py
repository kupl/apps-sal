def two_sort(array):
    array = sorted(array)
    s = array[0]
    s2 = ""
    for i in s:
        s2 += i + "***"
    s2 = s2.strip("***")
    return s2
