def char_to_put(c1, c2):
    if c1 == c2:
        return c1
    elif (c1 == 'B' and c2 == 'R') or (c1 == 'R' and c2 == 'B'):
        return 'G'
    elif (c1 == 'G' and c2 == 'R') or (c1 == 'R' and c2 == 'G'):
        return 'B'
    else:
        return 'R'


def compute(s):
    next_row = ""
    for i in range(0, len(s) - 1):
        next_row += char_to_put(s[i], s[i + 1])

    return next_row


def triangle(row):
    if len(row) == 1:
        return row[0]

    while len(row) != 1:
        row = compute(row)

    return row
