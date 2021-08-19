def rgb(r, g, b):

    def clamp(x):
        return max(0, min(x, 255))
    return '%02X%02X%02X' % (clamp(r), clamp(g), clamp(b))
