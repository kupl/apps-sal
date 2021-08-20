def connect_the_dots(s):
    s = list(map(list, s.splitlines()))
    arr = sorted(((v, i, j) for (i, row) in enumerate(s) for (j, v) in enumerate(row) if v.isalpha()))
    for ((_, y1, x1), (_, y2, x2)) in zip(arr, arr[1:]):
        (py, px) = (y1, x1)
        s[py][px] = '*'
        while (py, px) != (y2, x2):
            py += 1 if y2 > py else -1 if y2 < py else 0
            px += 1 if x2 > px else -1 if x2 < px else 0
            s[py][px] = '*'
    return '\n'.join(map(''.join, s)) + '\n'
