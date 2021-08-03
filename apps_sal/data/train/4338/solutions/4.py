def reverse_on_diagonals(a):
    for i in range(len(a) // 2):
        j = -1 - i
        a[i][i], a[j][j], a[i][j], a[j][i] = a[j][j], a[i][i], a[j][i], a[i][j]
    return a
