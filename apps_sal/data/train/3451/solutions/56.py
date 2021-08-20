from re import sub


def triangle(row):
    return row if len(row) == 1 else triangle(''.join((row[i] if row[i] == row[i + 1] else sub(f'[{row[i]}{row[i + 1]}]', '', 'RGB') for i in range(len(row) - 1))))
