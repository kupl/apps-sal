def next_char(pair):
    return set('RGB').difference(pair).pop() if pair[0] != pair[1] else pair[0]


def next_row(row):
    return "".join(map(next_char, zip(row, row[1:])))


def triangle(row):
    while len(row) > 1:
        row = next_row(row)
    return row
