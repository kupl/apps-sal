def nextt(a, b):
    if a == b:
        return a
    return 'RGB'.replace(a, '').replace(b, '')


def triangle(row):
    while len(row) > 1:
        t = ''
        for i in range(len(row) - 1):
            t = t + nextt(list(row)[i], list(row)[i + 1])
        row = t
    return row[0]
