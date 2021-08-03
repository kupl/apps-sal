def gen(a, b):
    d = {'BG': 'R', 'BR': 'G', 'GR': 'B'}
    return d.get(''.join(sorted([a, b])), a)


def triangle(row):
    a = [list(' ' * (len(row) - i)) for i in range(len(row))]
    a[0] = list(row)
    for i in range(0, len(row) - 1):
        for j in range(len(a[i]) - 1):
            a[i + 1][j] = gen(a[i][j], a[i][j + 1])
    return a[-1][0]
