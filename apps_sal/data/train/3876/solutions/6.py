def find(n):
    c_3 = n // 0x3
    c_5 = n // 0x5
    c_f = n // 0xf
    
    s_3 = c_3 * (0x3 + c_3 * 0x3) // 2
    s_5 = c_5 * (0x5 + c_5 * 0x5) // 2
    s_f = c_f * (0xf + c_f * 0xf) // 2
    
    return s_3 + s_5 - s_f

