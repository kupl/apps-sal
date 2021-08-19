def hex_hash(code):
    return sum((int(d) for c in code for d in f'{ord(c):x}' if d.isdecimal()))
