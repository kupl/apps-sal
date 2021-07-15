def pattern(n):
    if n == 1: return "1"
    if n < 1: return ""
    res = ""
    for i in range(0, n + 1, 1):
        res += (str(i) * i) + "\n"
    return "".join(res.strip())
