def animals(h, l):
    print(h, l)
    a = (4 * h - l) / 2
    b = h - a
    return (a, b) if a >= 0 and b >= 0 and (a == int(a)) and (b == int(b)) else 'No solutions'
