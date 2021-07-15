def rgb(r, g, b):
    def get_hex(s):
        if s > 255: s = 255
        if s < 0: s = 0
        return hex(s)[2:].upper() if len(hex(s)[2:]) > 1 else "0" + hex(s)[2:]
    return get_hex(r) + get_hex(g) + get_hex(b)

