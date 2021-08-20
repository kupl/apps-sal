def hex_hash(code):
    return sum((int(d) for d in ''.join(map(hex, map(ord, code))) if d.isdigit()))
