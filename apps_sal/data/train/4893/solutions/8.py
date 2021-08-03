def wave_sort(a):
    a.sort()
    array = []
    length = len(a)
    if len(a) <= 1:
        return 0
    for x in range(0, length // 2, 1):
        array.append(a[length - 1 - x])
        array.append(a[x])
    if len(a) % 2 != 0:
        array.insert(length - 1, a[int((length / 2))])
    for x in range(0, length):
        a[x] = array[x]
