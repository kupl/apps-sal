def expression_matter(a, b, c):
    d = a * (b + c)
    e = a * b * c
    f = a + b * c
    g = (a + b) * c
    h = a + b + c
    if (e >= d and e >= h) and (e >= f and e >= g):
        return e
    elif (d >= e and d >= h) and (d >= f and d >= g):
        return d
    elif (f >= d and f >= h) and (f >= e and f >= g):
        return f
    elif (g >= d and g >= h) and (g >= e and g >= f):
        return g
    elif (h >= d and h >= g) and (h >= e and h >= f):
        return h
