def seven(m, s=0):
    if m < 100: return (m, s)
    a, b = divmod(m, 10)
    return seven(a-2*b, s+1)
