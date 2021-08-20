def p_num(n):
    r = (1 + (24 * n + 1) ** 0.5) / 6
    return r.is_integer() and (3 * r ** 2 - r) / 2 == n


def g_p_num(n):
    r = (1 + 24 * n) ** 0.5 % 6
    return r != 0 and r.is_integer()


def s_p_num(n):
    return (n ** 0.5).is_integer() and p_num(n) and g_p_num(n)
