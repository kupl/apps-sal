val  = lambda c: ord(c.lower()) - (48 if ord(c) < 58 else 87)
int_ = lambda s, x: sum(val(c) * x**i for i,c in enumerate(reversed(s)))

def bin_to_hex(binary_string):
    return "{:x}".format(int_(binary_string, 2))
    
def hex_to_bin(hex_string):
    return "{:b}".format(int_(hex_string, 16))
