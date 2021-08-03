def hungry_seven(arr):
    i, a = 0, arr[:]
    while i < len(a) - 2:
        if i >= 0 and a[i:i + 3] == [7, 8, 9]:
            a[i:i + 3] = [8, 9, 7]
            i -= 2
        i += 1
    return a
