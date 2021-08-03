def derive(c, e):
    if e <= 2:
        e = 3
    return f"{c * e}x^{e - 1}"
