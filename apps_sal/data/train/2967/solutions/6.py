N = '0123456789abcdef'

def converter(s, p1, p2):
    """ Convert input string to desired output """
    dec = sum(N.find(s[~i].lower()) * (p1 ** i) for i in range(len(s)))
    res = []
    while dec != 0:
        res.append(dec % p2)
        dec //= p2
    return ''.join(N[i] for i in reversed(res)) if res else '0'

def bin_to_hex(b):
    return converter(b, 2, 16)
    
def hex_to_bin(h):
    return converter(h, 16 ,2)
