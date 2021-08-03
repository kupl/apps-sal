def pattern(n):
    if n < 1:
        return ''
    s = ""
    d = ""
    for i in range(1, n + 1):
        s += d + str(i) * i
        d = "\n"
    return s
