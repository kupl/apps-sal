def f(ar, col):
    for row in ar:
        if col < len(row) and row[col] == '1':
            col += 1
        elif col > 0 and row[col - 1] == '1':
            col -= 1
    return col


def amidakuji(ar):
    return [f(ar[::-1], col) for col in range(len(ar[0]) + 1)]
