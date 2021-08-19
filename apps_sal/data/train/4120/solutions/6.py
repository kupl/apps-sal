def sort_dict(d):
    a = []
    for x in d:
        a.append((x, d[x]))
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i][1] < a[j][1]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    return a
