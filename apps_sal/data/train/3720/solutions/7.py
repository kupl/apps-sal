def hex_hash(code):
    r = 0
    for c in code:
        for d in hex(ord(c))[2:]:
            if d.isdigit():
                r += int(d)
    return r
