def hex_con(color):
    hex_dict = '0123456789ABCDEF'
    d1 = color//16
    d2 = color%16
    if d1 > 15:
        d1 = 15
        d2 = 15
    elif d1 < 0:
        d1 = 0
        d2 = 0
    return str(hex_dict[d1]) + str(hex_dict[d2])
    


def rgb(r, g, b):  
    R = hex_con(r)
    G = hex_con(g)
    B = hex_con(b)
    return R+G+B
