def hex_hash(code):
    return sum(sum(int(d) for d in hex(ord(c)) if d.isdigit()) for c in code)
