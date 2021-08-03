def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(clamp(r), clamp(g), clamp(b))


def clamp(x):
    return max(0, min(x, 255))
