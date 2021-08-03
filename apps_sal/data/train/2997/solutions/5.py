def rgb(r, g, b):
    return ''.join(['%02X' % max(0, min(x, 255)) for x in [r, g, b]])
