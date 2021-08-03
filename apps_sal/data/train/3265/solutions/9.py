def mult_triangle(n):
    c, o = 0, 0
    for i in range(1, n + 1):
        v = i**2
        c += i * v
        if i & 1:
            o += i * (v + 1 >> 1)
    return [c, c - o, o]
