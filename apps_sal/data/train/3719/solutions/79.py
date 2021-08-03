def starting_mark(height):

    h1 = 1.52
    d1 = 9.45

    h2 = 1.83
    d2 = 10.67

    v = (d2 - d1) / (h2 - h1)

    return round(d2 - v * (h2 - height), 2)
