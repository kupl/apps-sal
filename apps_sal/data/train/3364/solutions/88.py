def predict_age(a, b, c, d, e, f, g, h):
    r = [a, b, c, d, e, f, g, h]
    rs = int(sum([i ** 2 for i in r]) ** 0.5 / 2)
    return rs
