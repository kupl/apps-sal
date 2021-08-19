def make_upper_case(st):
    out = ''
    for s in st:
        o = ord(s)
        if 97 <= o <= 122:
            o -= 32
        out += chr(o)
    return out
