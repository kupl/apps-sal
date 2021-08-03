colors = set('RGB')


def triangle(row):
    while len(row) > 1:
        row = [a if a == b else colors.difference(a).difference(b).pop() for a, b in zip(row, row[1:])]
    return row[0]
