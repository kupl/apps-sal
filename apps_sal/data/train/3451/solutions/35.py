def triangle(row):
    row = ['RGB'.index(char) + 1 for char in row]
    while len(row) > 1:
        row = [row[i] ^ row[i - 1] or row[i] for i in range(1, len(row))]
    return 'RGB'[row[0] - 1]
