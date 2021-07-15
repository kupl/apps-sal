def rgb(r, g, b):
    clamp = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))
