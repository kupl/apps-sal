from math import floor


def peak_height(mountain):
    a = []
    for i in mountain:
        b = []
        for j in i:
            if j == ' ':
                b.append(0)
            else:
                b.append(1)
        a.append(b)

    for m in range(floor(min(len(a), len(a[0])) / 2)):
        for i in range(1 + m, len(a) - 1 - m):
            for j in range(1 + m, len(a[0]) - 1 - m):
                if a[i][j] > 0:
                    a[i][j] = min(a[i - 1][j], a[i + 1][j], a[i][j - 1], a[i][j + 1]) + 1

    return max([max(i) for i in a])
