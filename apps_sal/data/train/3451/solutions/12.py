def possibilities(a, b):
    c = abs(ord(a) - ord(b))
    if c == 0:
        return a
    if c == 5:
        return 'R'
    if c == 11:
        return 'B'
    if c == 16:
        return 'G'
    return None


def triangle(row):

    while len(row) > 1:
        temp = ''
        for i in range(len(row) - 1):
            temp += possibilities(row[i], row[i + 1])
        row = temp

    return row[0]
