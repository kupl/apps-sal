def hex_hash(code):
    return sum((int(d) for d in ''.join((hex(ord(c)) for c in code)) if d.isdigit()))
