
def fixed_xor(a, b):
    if a == "" or b == "":
        return ""

    m = min(len(a), len(b))
    ha = int(a[:m], 16)
    hb = int(b[:m], 16)

    return hex(ha ^ hb)[2:].zfill(m)
