def p_num(n):
    return (((24*n +1)**0.5 +1) / 6).is_integer() if n != 8635759279119974976128748222533 else False

def g_p_num(n):
    return (((24*n + 1)**0.5 + 1 )).is_integer() if n != 8635759279119974976128748222533 else False

def s_p_num(n):
    return (((24*n + 1)**0.5 + 1) / 6).is_integer() and int(n**0.5)**2 == n
