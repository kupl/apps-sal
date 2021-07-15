def two_sort(array):
    print(array)
    temp = min(array)
    print(temp)
    res = ""
    for x in temp:
        res += x + "***"
    return res.rstrip("*")
