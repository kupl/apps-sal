def triangle(row):
    # r = []
    # a = list(row)
    print(row)
    r = ''
    a = row[:]
    if len(a) == 1:
        return a
    for i in range(len(a) - 1):
        # t = ['R','G','B']
        t = 'RGB'
        if a[i] == a[i + 1]:
            # r.append(a[i])
            r += a[i]
        else:
            # t.remove(a[i])
            # t.remove(a[i+1])
            # r.append(t[0])
            t = t.replace(a[i], '').replace(a[i + 1], '')
            r += t

    return triangle(r)
