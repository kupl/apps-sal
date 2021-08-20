def find(n):
    c_3 = n // 3
    c_5 = n // 5
    c_f = n // 15
    s_3 = c_3 * (3 + c_3 * 3) // 2
    s_5 = c_5 * (5 + c_5 * 5) // 2
    s_f = c_f * (15 + c_f * 15) // 2
    return s_3 + s_5 - s_f
