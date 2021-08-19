def colour(a, b):
    if a == b:
        return a
    elif a == 'B' and b == 'G' or (a == 'G' and b == 'B'):
        return 'R'
    elif a == 'R' and b == 'G' or (a == 'G' and b == 'R'):
        return 'B'
    elif a == 'B' and b == 'R' or (a == 'R' and b == 'B'):
        return 'G'


def triangle(row):
    if len(row) < 2:
        return row
    else:
        rez = []
        for i in range(0, len(row) - 1):
            rez.append(colour(row[i], row[i + 1]))
        l = len(rez)
        if l > 1:
            rez = triangle(rez)
        return ''.join(rez)
