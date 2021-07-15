def p_num(n):
    k = int((1 + (1 + 24 * n) ** 0.5) / 6)
    return n > 0 and k * (3 * k - 1) == 2 * n
    
def g_p_num(n):
    k = int((1 - (1 + 24 * n) ** 0.5) / 6)
    return k * (3 * k - 1) == 2 * n or p_num(n)
    
def s_p_num(n):
    return n ** 0.5 % 1 == 0 and p_num(n)
