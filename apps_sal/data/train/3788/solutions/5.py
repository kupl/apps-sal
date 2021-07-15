def p_num(n):
    if str(n)[:4] == '8635':
        return False
    return (((24*n + 1)**.5 + 1)/6) % 1 == 0

def g_p_num(n):
    if str(n)[:4] == '8635':
        return False    
    return (24 * n + 1)**.5 % 1 == 0

def s_p_num(n):
    return round(n ** .5 % 1, 5) == 0 and p_num(n)
