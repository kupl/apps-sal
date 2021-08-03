def nth_smallest(list1, num):
    a = list(list1)
    a.sort()
    return a[num - 1]
