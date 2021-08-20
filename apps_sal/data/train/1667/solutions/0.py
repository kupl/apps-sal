def unflatten(m, d, c=0):
    return m if c == d else unflatten(parse(m, [0, 1][c & 1]), d, c + 1)


def parse(ar, lr):
    (sub, i) = ([], [0, len(ar) - 1][lr])
    while 0 <= i < len(ar):
        (j, r) = (ar[i], lr == 1)
        if isinstance(j, list):
            sub.append(parse(j, lr))
            i += [1, -1][r]
        else:
            mod = j % len([ar[i:], ar[:i + 1]][r])
            sub.append([j, ar[i:i + mod * [1, -1][r]:[1, -1][r]][::[1, -1][r]]][mod >= 3])
            i += [mod, 1][mod < 3] * [1, -1][r]
    return sub[::[1, -1][lr]]
