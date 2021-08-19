# I defined these vars to make it more updateable if the input format changes
red = 'R'
blu = 'B'
gre = 'G'


def add(col1, col2):
    # Two same colors add to same color:
    if col1 == col2:
        return col1
    # BG returns R (order doesn't matter)
    elif (col1 == blu or col1 == gre) and (col2 == blu or col2 == gre):
        return red
    # RG returns B
    elif (col1 == red or col1 == gre) and (col2 == red or col2 == gre):
        return blu
    # RB returns G
    elif (col1 == blu or col1 == red) and (col2 == blu or col2 == red):
        return gre


def triangle(row):
    if(row == None):
        return None
    row = list(row)
    l = len(row)
    # check base cases first: with n=1, n=2
    if(l == 0):
        return None
    if(l == 1):
        return row[0]
    if(l == 2):
        return add(row[0], row[1])
    # with n > 1, add(i, i+1) until n-1
    for i in range(0, l - 1):
        row[i] = add(row[i], row[i + 1])
    # get rid of the old nth term left from calculating the new row's nth term
    row.pop()
    # then recurse:
    return triangle(row)
