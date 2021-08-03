bh = {"": "", "0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7", "1000": "8", "1001": "9", "1010": "a", "1011": "b", "1100": "c", "1101": "d", "1110": "e", "1111": "f"}


def bin_to_hex(bs):
    r = ""
    bs = "000" + bs
    for i in range(len(bs), -1, -4):
        s = bs[i - 4:i]
        r = bh[s] + r
    while r[0] == "0" and len(r) > 1:
        r = r[1:]
    return r


hb = {bh[v]: v for v in bh}


def hex_to_bin(hs):
    r = ""
    hs = hs.lower()
    for c in hs:
        r += hb[c]
    while r[0] == "0" and len(r) > 1:
        r = r[1:]
    return r
