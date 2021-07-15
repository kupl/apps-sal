def hex_hash(code):
    return sum(int(d) for c in code for d in hex(ord(c)) if d.isdigit())
