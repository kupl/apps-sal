red = 'R'
blu = 'B'
gre = 'G'


def add(col1, col2):
    if col1 == col2:
        return col1
    elif (col1 == blu or col1 == gre) and (col2 == blu or col2 == gre):
        return red
    elif (col1 == red or col1 == gre) and (col2 == red or col2 == gre):
        return blu
    elif (col1 == blu or col1 == red) and (col2 == blu or col2 == red):
        return gre


def triangle(row):
    if(row == None):
        return None
    row = list(row)
    l = len(row)
    if(l == 0):
        return None
    if(l == 1):
        return row[0]
    if(l == 2):
        return add(row[0], row[1])
    for i in range(0, l - 1):
        row[i] = add(row[i], row[i + 1])
    row.pop()
    return triangle(row)
