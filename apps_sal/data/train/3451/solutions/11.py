def mod3(n):
    c = 0
    while n % 3 == 0:
        n /= 3
        c += 1
    return int(n % 3), c


def triangle(row):
    rgb = {'R': 0, 'G': 1, 'B': 2}
    RGB = "RGB"
    n = len(row)
    x, y = 1, 0
    res = rgb[row[0]]
    for i in range(1, n):
        xx, yy = mod3(n - i)
        x = x * xx % 3
        y += yy
        xx, yy = mod3(i)
        x = x * xx % 3
        y -= yy
        if y == 0:
            res += rgb[row[i]] * x
    res %= 3
    if n % 2 == 0:
        res = (3 - res) % 3
    return RGB[res]
