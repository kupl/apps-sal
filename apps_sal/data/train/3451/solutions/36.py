def triangle(row):
    a = {153: 'B', 148: 'G', 137: 'R', 164: 'R', 142: 'G', 132: 'B', 82: 'R', 71: 'G', 66: 'B'}
    b = list(row)
    while len(b) > 1:
        b = list(map(ord, b))
        b = [a[b[i] + b[i + 1]] for i in range(len(b) - 1)]
    return b[0]
