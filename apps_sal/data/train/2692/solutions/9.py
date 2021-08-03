def bubble(a):
    if a == None or len(a) < 2:
        return []
    swapped = True
    i = 0
    r = []
    while i < len(a) - 1 and swapped:
        swapped = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                r.append(list(a))
                swapped = True
        i += 1
    return r
