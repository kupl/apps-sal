def get_candy_position(a, row, col, candy):
    from math import ceil
    bx_sz = row * col
    if row * col < a:
        n = ceil(a / (row * col)) * (col * row)
    else:
        n = row * col
    l = [i if i <= a else 'X' for i in list(range(1, n - n % row + 1))]
    split_l = [list(l[i:i + bx_sz])[::-1] for i in range(0, len(l), bx_sz)]
    b = [i[j:j + col] for i in split_l for j in range(0, len(i), col)]
    c = [b[i:i + row] for i in range(0, len(b), row)]
    for i in range(len(c)):
        for j in range(len(c[i])):
            for k in range(len(c[i][j])):
                if c[i][j][k] == candy:
                    return [i + 1, j, k]
    return [-1, -1, -1]
