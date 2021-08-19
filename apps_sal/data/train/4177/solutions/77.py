def men_from_boys(arr):
    m = []
    b = []
    for i in arr:
        if i % 2 == 0:
            if i not in m:
                m.append(i)
        elif i not in b:
            b.append(i)
    m.sort()
    b.sort(reverse=True)
    for i in b:
        m.append(i)
    return m
