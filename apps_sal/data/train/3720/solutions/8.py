def hex_hash(code):
    res = ''.join(list(map(hex, map(ord, code))))
    return sum((int(x) for x in res if x.isdigit()))
