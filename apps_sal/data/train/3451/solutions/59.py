def triangle(row):
    print(row)
    r = ''
    a = row[:]
    if len(a) == 1:
        return a
    for i in range(len(a) - 1):
        t = 'RGB'
        if a[i] == a[i + 1]:
            r += a[i]
        else:
            t = t.replace(a[i], '').replace(a[i + 1], '')
            r += t
    return triangle(r)
