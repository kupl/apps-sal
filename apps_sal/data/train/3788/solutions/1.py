def get_p(n):
    mean = round((n * 2 / 3)**0.5)
    base = 3 * mean**2 // 2
    return {"strict": base - mean // 2, "generalized": base + (mean + 1) // 2}


def p_num(n):
    return n and get_p(n)["strict"] == n


def g_p_num(n):
    return n in get_p(n).values()


def s_p_num(n):
    return p_num(n) and not (n**0.5 % 1)
